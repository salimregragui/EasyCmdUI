import os
import time
import keyboard


class EasyCmdUi:
    '''Class that makes creating cmd ui's easier'''

    def __init__(self, config):
        self.width = config.get("width")  # the max width of the cmd
        self.height = config.get("height") - 4  # the max height of the cmd
        # boolean that determines if the content on the cmd can scroll past the max height
        self.fixed = config.get("fixed")
        self.bordered = config.get("bordered")  # boolean that determines if the ui has borders
        # boolean that determines if the ui content is centered in the cmd
        self.centered = config.get("centered")
        self.adjust = config.get("adjust")#boolean that determines if the ui borders end on last content or on height
        self.displays = []  # list that stocks all the contents page per page if the ui is fixed
        self.content = []  # all the content of the current display
        self.stylized_content = [] #all the content stylized
        self.working_width = self.width  # width of the actual ui
        self.centering_size = 0  # how many spaces we need to add to center the ui

        if self.centered:  # if the dev wants the ui to be centered in the cmd
            self.working_width = self.width - 10
            self.centering_size = 5

    def slow_print(self, text):
        '''Function that shows a string character by character'''
        slow_text = True  # bool that determines if we show character by character

        for i, char in enumerate(text):
            # if the user types space we show all the text without slowing
            if keyboard.is_pressed('space'):
                slow_text = False

            os.sys.stdout.write(char)  # we show the current character
            os.sys.stdout.flush()

            if slow_text and char != " ": #if the user didn't click on space and the character to be displayed is not a space
                time.sleep(.02)

        print("")

    def apply_styling(self, sentence):
        '''method that applies selected styling to string'''

        #we remove all the spaces from the styling
        sentence["styling"] = sentence["styling"].replace(" ", "")
        #we create a list of all the styles chosen
        styles = sentence["styling"].split("|")
        text = sentence["text"] #the text to display

        if "indented" in styles:
            text = "    " + text #if the dev wants an indentation we add spaces to the start
        
        if "upper" in styles:
            text = text.upper() #if the dev wants the text to be all uppercase

        if "lower" in styles:
            text = text.lower()

        if "capitalize" in styles:
            text = text.capitalize()

        if "centered" in styles: #if the dev wants the text centered inside the ui
            text = text.strip() #we remove all the trailing whitespaces
            spaces_size = self.working_width - len(text) #we determine how many spaces we need to add to center the text

            for i in range(1, int(spaces_size / 2) + 1): #we add the spaces necessary to the text
                text = " " + text

        if "newline" in styles: #if the dev wants to add an empty line after this one
            return (text, True)

        return (text, False) #we return a tuple that contains the text and if there is a newline

    def sentence_to_ui_object(self, sentence):
        '''method that transforms a ui sentence given by user to an object that can be doctored ad stylized'''
        sentence = sentence.split("|")

        sentence[0] = sentence[0].replace(" ", "")
        styles = sentence[0].split(",")
        new_styles_list = []

        for style in styles:
            if style == "nl":
                new_styles_list.append(style.replace("nl", "newline"))
            elif style == "c":
                new_styles_list.append(style.replace("c", "centered"))
            elif style == "u":
                new_styles_list.append(style.replace("u", "upper"))
            elif style == "l":
                new_styles_list.append(style.replace("l", "lower"))
            elif style == "ul":
                new_styles_list.append(style.replace("ul", "underline"))
            elif style == "i":
                new_styles_list.append(style.replace("i", "indented"))

        sentence[1] = sentence[1].replace("f", "") #an empty string will be converted to false
        sentence[1] = sentence[1].replace("t", "True")

        sentence[2] = sentence[2].replace("p", "paragraph")
        sentence[2] = sentence[2].replace("s", "sentence")

        new_ui_object = {
            "text" : sentence[3],
            "styling": "|".join(new_styles_list),
            "slow": bool(sentence[1]),
            "type": sentence[2]
        }

        return new_ui_object

    def add_content(self, content):
        '''method that allows the dev to add content to show in the ui'''
        if isinstance(content, str): #if the user chose the string style we transform it into an object
            self.content.append(self.sentence_to_ui_object(content))

        else:
            self.content.append(content)

    def doctor_content(self, content):
        '''method that breaks down lines to the maximum of the working space and adds newlines when necessary'''
        new_content_list = [] #a list that will stock all the content broken down into the size chosen by the dev

        #foreach object in the content list
        for contentid, content_val in enumerate(content):
            space_to_remove = 0 #how many spaces we need to remove to stylize the content

            if self.bordered and self.centered:
                space_to_remove = space_to_remove + 2

            if self.bordered and not self.centered or self.centered and not self.bordered:
                space_to_remove = space_to_remove + 3

            if "centered" in content_val["styling"]: #if the content is stylized with centered
                space_to_remove = space_to_remove + 10

            if "indented" in content_val["styling"]:
                space_to_remove = space_to_remove + 6

            #if the text in the content is bigger than the autorized width
            if len(content_val["text"]) >= self.working_width - space_to_remove:
                current_sentence = "" #the current sentence from the paragraph
                sentences_counter = 0 #counter of the number of sentences this paragraph will be split into
                counter = 0 #variable that counts the number of letters that we have gone throught
                beginning_of_sentence = False #boolean that checks if we are at the start of a sentence
                for letter in content_val["text"]:
                    #if we arrive at the letter that is over the space allowed for the ui or we encounter a go to line character
                    if counter % (self.working_width - space_to_remove) == 0 and counter != 0 or letter == '~':
                        if letter not in (" ", "~"):
                            current_sentence = current_sentence + letter

                        #we add the current sentence to the content list
                        new_content_list.append(dict(text=current_sentence, styling=content_val["styling"].replace("newline", ""), slow=content_val["slow"], type=content_val["type"]))
                        current_sentence = "" #we reset the current sentence and add 1 to the sentences from paragraph
                        sentences_counter = sentences_counter + 1
                        beginning_of_sentence = True
                    else:
                        if beginning_of_sentence and letter == " ": #if the first letter in the new sentence is a space
                            beginning_of_sentence = False
                        else:
                            current_sentence = current_sentence + letter
                            beginning_of_sentence = False

                    counter = counter + 1 #we increment the counter of letter gone throught

                #we insert the rest of the characters left from the split
                new_content_list.append(dict(text=current_sentence, styling=content_val["styling"], slow=content_val["slow"], type=content_val["type"]))
            else:
                #if the content is conform we just append it to the new list
                new_content_list.append(dict(text=content_val["text"], styling=content_val["styling"], slow=content_val["slow"], type=content_val["type"]))
        return new_content_list

    def centerer(self, width):
        '''method that returns the number of spaces needed to center a content'''
        spaces_needed = ""

        for i in range(0, width):
            spaces_needed = spaces_needed + " "

        return spaces_needed

    def ending_boxing(self, sentence):
        '''method that adds the pipe at the end for a boxed ui'''
        ending_addition = ""

        ending_range = self.working_width - len(sentence)

        if self.working_width == self.width:
            ending_range = ending_range - 1

        for i in range(0, ending_range):
            ending_addition = ending_addition + " "

        ending_addition = ending_addition + "|"
        return ending_addition

    def display(self):
        '''method that displays the ui'''

        if self.bordered:
            print(self.centerer(self.centering_size), end="")
            for i in range(
                    0,
                    self.working_width):  # loop that displays the top border
                print("-", end="")

            if self.working_width != self.width:
                print("")

        self.content = self.doctor_content(self.content)

        #stylizing every single sentence and stocking the result in the corresponding list
        for cont in self.content:
            stylized_text, has_newline = self.apply_styling(cont) #we store the returned tuple into two variables
            self.stylized_content.append(stylized_text) #we store the stylized text into the list

            if has_newline: #if the sentence has the newline styling option
                self.stylized_content.append("")

        for j in self.stylized_content:  # loop that displays all the content in the ui
            if self.working_width != self.width:
                if self.bordered:
                    print(self.centerer(self.centering_size) +"|" +j +self.ending_boxing("|" + j))
                else:
                    print(self.centerer(self.centering_size) + j)
            else:
                if self.bordered:
                    print(self.centerer(self.centering_size) +"|" +j +self.ending_boxing("|" +j), end="")
                else:
                    print(self.centerer(self.centering_size) + j)

        if self.bordered:
            if not self.adjust:
                for h in range(0, self.height - len(self.content)):  # loop that adds empty lines to complete the ui
                    if self.working_width != self.width:
                        print(self.centerer(self.centering_size) + "|" + self.ending_boxing("|"))
                    else:
                        print(self.centerer(self.centering_size) + "|" + self.ending_boxing("|"), end="")

            print(self.centerer(self.centering_size), end="")
            for k in range(
                    0,
                    self.working_width):  # loop that displays the end border
                print("-", end="")
