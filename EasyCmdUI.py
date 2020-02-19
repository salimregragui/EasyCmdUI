import os
import time
import keyboard
import tabulate


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

        if "inherit" in styles:
            #foreach content in the list if the id is the same as the one we are applying style to
            master_style = "" #we get the style of the container of this element

            for cont in self.content:
                if cont["contentid"] == sentence["contentid"]:
                    master_style = cont["styling"]
                    break

            #we remove all the spaces from the styling
            master_style = master_style.replace(" ", "")
            #we create a list of all the styles chosen
            styles = master_style.split("|")

        if "indented" in styles:
            text = "    " + text #if the dev wants an indentation we add spaces to the start
        
        if "upper" in styles:
            text = text.upper() #if the dev wants the text to be all uppercase

        if "lower" in styles:
            text = text.lower()

        if "capitalize" in styles:
            text = text.capitalize()

        if "centered" in styles and "centered-left" not in styles: #if the dev wants the text centered inside the ui
            text = text.strip() #we remove all the trailing whitespaces
            spaces_size = (self.working_width - len(text)) / 2 #we determine how many spaces we need to add to center the text

            if not spaces_size.is_integer():
                spaces_size = int(spaces_size) + 1

            for i in range(1, int(spaces_size)): #we add the spaces necessary to the text
                text = " " + text

        if "centered-left" in styles and "centered" not in styles: #if the dev wants the text centered inside the ui
            all_texts_in_content = [] #variable that will stock all the sentences in this multiline paragraph

            #foreach content in the list if the id is the same as the one we are applying style to
            for cont in self.content:
                if cont["contentid"] == sentence["contentid"]:
                    all_texts_in_content.append(cont["text"])

            longest_sentence = len(max(all_texts_in_content, key=len)) #we select the length of the longest sentence

            text = text.strip() #we remove all the trailing whitespaces
            spaces_size = (self.working_width - longest_sentence) / 2 #we determine how many spaces we need to add to center the text

            if not spaces_size.is_integer():
                spaces_size = int(spaces_size) + 1

            for i in range(1, int(spaces_size)): #we add the spaces necessary to the text
                text = " " + text

        if "li" in styles:
            text = "  " + text

        if "nli" in styles:
            text = "    " + text

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

            elif style == "c-l":
                new_styles_list.append(style.replace("c-l", "centered-left"))

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

    def sentence_slicing(self, sentence, id):
        '''method that takes a sentence and slices it into multiple ones tha fit the ui'''
        content_list = []
        space_to_remove = 0 #how many spaces we need to remove to stylize the content

        if self.bordered and self.centered:
            space_to_remove = space_to_remove + 2

        if self.bordered and not self.centered or self.centered and not self.bordered:
            space_to_remove = space_to_remove + 3

        if "centered" in sentence["styling"]: #if the content is stylized with centered
            space_to_remove = space_to_remove + 10

        if "indented" in sentence["styling"]:
            space_to_remove = space_to_remove + 6

        if "li" in sentence["styling"]:
            space_to_remove = space_to_remove + 5

        if "nli" in sentence["styling"]:
            space_to_remove = space_to_remove + 7

        #if the text in the content is bigger than the autorized width
        current_sentence = "" #the current sentence from the paragraph
        sentences_counter = 0 #counter of the number of sentences this paragraph will be split into
        counter = 0 #variable that counts the number of letters that we have gone throught
        beginning_of_sentence = False #boolean that checks if we are at the start of a sentence
        for letter in sentence["text"]:
            #if we arrive at the letter that is over the space allowed for the ui or we encounter a go to line character
            if (counter % (self.working_width - space_to_remove) == 0 and counter != 0) or letter == "~":
                if letter not in (" ", "~"):
                    current_sentence = current_sentence + letter

                #we add the current sentence to the content list
                content_list.append(dict(text=current_sentence, styling=sentence["styling"].replace("newline", ""), slow=sentence["slow"], type=sentence["type"], multiline=True, contentid=id))
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
        content_list.append(dict(text=current_sentence, styling=sentence["styling"], slow=sentence["slow"], type=sentence["type"], multiline=True, contentid=id))

        return content_list

    def doctor_content(self, content):
        '''method that breaks down lines to the maximum of the working space and adds newlines when necessary'''
        new_content_list = [] #a list that will stock all the content broken down into the size chosen by the dev

        #foreach object in the content list
        for contentid, content_val in enumerate(content):
            new_content_list = new_content_list + self.sentence_slicing(content_val, contentid)

            if content_val["type"] == "list": #if the element is a list
                #we loop throught each element of the list and make it a content
                for list_content_id, list_content_val in enumerate(content_val["list items"]):
                    list_object = {}
                    if isinstance(list_content_val, str): #if the dev chose to send just a string
                        list_object["text"] = list_content_val
                        list_object["styling"] = "inherit"
                        list_object["type"] = "sentence"
                        list_object["slow"] = True
                    else:
                        list_object = list_content_val #if the dev sent an object
                        list_object["styling"] = list_object["styling"] + "| li"

                    if "inherit" in list_object["styling"]:#if the dev chose to inherit the styling from the parent content
                        list_object["styling"] = content_val["styling"] + "| li"

                    #we add the number of the li to the text
                    list_object["text"] = str(list_content_id + 1) + ". " + list_object["text"]

                    if list_object["type"] == "sentence":
                        new_content_list = new_content_list + self.sentence_slicing(list_object, contentid)

                    #if the user sent a list to the content
                    elif list_object["type"] == "list":
                        new_content_list = new_content_list + self.sentence_slicing(list_object, contentid)
                        for nested_list_content_id, nested_list_content_val in enumerate(list_content_val["list items"]):
                            nested_list_object = {}
                            if isinstance(nested_list_content_val, str): #if the dev chose to send just a string
                                nested_list_object["text"] = nested_list_content_val
                                nested_list_object["styling"] = "inherit"
                                nested_list_object["type"] = "sentence"
                                nested_list_object["slow"] = True
                            else:
                                nested_list_object = nested_list_content_val #if the dev sent an object
                            nested_list_object["styling"] = nested_list_object["styling"] + "| nli"

                            if "inherit" in nested_list_object["styling"]:#if the dev chose to inherit the styling from the parent content
                                nested_list_object["styling"] = content_val["styling"] + "| nli"

                            #we add the number of the li to the text
                            nested_list_object["text"] = str(list_content_id + 1) + "." + str(nested_list_content_id + 1) + ". " + nested_list_object["text"]
                            new_content_list = new_content_list + self.sentence_slicing(nested_list_object, contentid)


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
            for i in range(0,self.working_width):  # loop that displays the top border
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
