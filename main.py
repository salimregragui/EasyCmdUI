import UITypes
import EasyCmdUI

CONFIG = {
    "width" : 96,
    "height" : 30,
    "fixed" : True,
    "bordered" : True,
    "centered" : False,
    "adjust" : True
}

UI = EasyCmdUI.EasyCmdUi(CONFIG)

UI.add_content({
    "text": "DETECTIVE PYTHON - THE GAME AND THE ADVENTURES of the new lord of the world so that's how it works !",
    "styling": "newline | upper | underline | centered",
    "slow": True,
    "type": "sentence"
})

UI.add_content({
    "text": "MY list :",
    "styling":"capitalize | indented",
    "slow":True,
    "type":"list",
    "list items": [
        "First item oh and it is a rather long one you feel me i don't think it could be slowed down to a realistic amount of shots you see my man it's hard",
        {
            "text" : "Second item",
            "slow" : True,
            "styling": "inherit",
            "type":"sentence"
        },
        {
            "text": "Nested list :",
            "styling": "inherit",
            "slow": "true",
            "type":"list",
            "list items": [
                "Oh a nested list !",
                {
                    "text": "Yeah it's rather nested if i may say",
                    "styling": "inherit",
                    "slow" : "true",
                    "type":"sentence"
                }
            ]
        },
        {
            "text": "Nested list :",
            "styling": "inherit",
            "slow": "true",
            "type":"list",
            "list items": [
                "Oh a nested list !",
                {
                    "text": "Yeah it's rather nested if i may say",
                    "styling": "inherit",
                    "slow" : "true",
                    "type":"sentence"
                }
            ]
        }
    ]
})

UI.add_content("l,i,c, nl|t|s|hola another~ line to be~ centered")
UI.add_content("l,c,nl|t|s|Let's add a full paragraph and see how it looks when the library beautifies it and makes it more adequate for a good ui !")
UI.add_content("u,i,c,nl|t|s|Let's add a full~ paragraph and see how it looks when the library beautifies it and makes it more adequate for a good ui !")
UI.add_content("u,i,c-l,nl|t|s|Let's add a full paragraph and see how it looks when the library beautifies it and makes it more adequate for a good ui ! the result is quite beautiful if I may say so myself :)")
UI.add_content("u,i,c-l,nl|t|s|Omnis eum ut fuga adipisci debitis. Labore ex quia voluptas facere.A Odit tempora est nisi inventore in excepturi voluptas vel. Ut sint eos velit non dolor voluptatem. Et dolore eum.")
print("")
UI.display()

# UIText = UITypes.UIText("test text that will be displayed in the~ui :)").style("nl,u").is_slow()
# UIText.astyle("i")

# UI.add_element(UIText)
# UI.add_element(UITypes.UIText("oh look a new line").style("u,i").is_slow())
# UI.display()