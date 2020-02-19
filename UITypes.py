class UIElement:
    def __init__(self, text):
        self.content = text
        self.styling = ""
        self.slow = False
        self.stylized_content = ""

    def doctor_content(self):
        pass

    def style(self, styling):
        '''method that applies styling to the ui object'''

        styles = styling.split(",")
        new_styles_list = []

        for style in styles:
            if style == "nl" and "newline" not in new_styles_list:
                new_styles_list.append(style.replace("nl", "newline"))

            elif style == "c" and "centered" not in new_styles_list:
                new_styles_list.append(style.replace("c", "centered"))

            elif style == "u" and "upper" not in new_styles_list:
                new_styles_list.append(style.replace("u", "upper"))

            elif style == "l" and "lower" not in new_styles_list:
                new_styles_list.append(style.replace("l", "lower"))

            elif style == "ul" and "underline" not in new_styles_list:
                new_styles_list.append(style.replace("ul", "underline"))

            elif style == "i" and "indented" not in new_styles_list:
                new_styles_list.append(style.replace("i", "indented"))

            elif style == "c-l" and "centered-left" not in new_styles_list:
                new_styles_list.append(style.replace("i", "centered-left"))

        self.styling = "|".join(new_styles_list)

        return self

    def astyle(self, styling):
        '''method that adds a style to the already defined styles'''
        styles = styling.split(",")
        new_styles_list = []

        for style in styles:
            if style == "nl" and "newline" not in self.styling and "newline" not in new_styles_list:
                new_styles_list.append(style.replace("nl", "newline"))

            elif style == "c" and "centered" not in self.styling and "centered" not in new_styles_list:
                new_styles_list.append(style.replace("c", "centered"))

            elif style == "u" and "upper" not in self.styling and "upper" not in new_styles_list:
                new_styles_list.append(style.replace("u", "upper"))

            elif style == "l" and "lower" not in self.styling and "lower" not in new_styles_list:
                new_styles_list.append(style.replace("l", "lower"))

            elif style == "ul" and "underline" not in self.styling and "underline" not in new_styles_list:
                new_styles_list.append(style.replace("ul", "underline"))

            elif style == "i" and "indented" not in self.styling and "indented" not in new_styles_list:
                new_styles_list.append(style.replace("i", "indented"))

        self.styling = self.styling + "|" + "|".join(new_styles_list)

        return self

    def is_slow(self):
        '''method that makes the UIelement slow written'''
        self.slow = True
        
        return self

    def nslow(self):
        '''method that makes the UIelement not slow written'''
        self.slow = False

        return self

    def objectify(self):
        '''method that returns the uielement data as an object'''
        return {
            "content" : self.content,
            "styling" : self.styling,
            "slow" : self.slow,
            "stylized content" : self.stylized_content
        }

    def get_styling(self):
        return self.styling

    def get_content(self):
        return self.content

    def get_stylized_content(self):
        return self.stylized_content

    def display(self):
        print(self.content)
        print(self.styling)
        print(self.slow)

class UIText(UIElement):
    '''a ui text that can be a sentence or a paragraph'''

class UIList(UIElement):
    '''a ui list that contains texts or nested lists'''

class UITable(UIElement):
    '''a ui table that contains rows and columns'''
