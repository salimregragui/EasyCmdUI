import UITypes
import EasyCmdUI

CONFIG = {
    "width" : 95,
    "height" : 30,
    "fixed" : True,
    "bordered" : True,
    "centered" : True,
    "adjust" : True
}

UI = EasyCmdUI.EasyCmdUi(CONFIG)

UIText = UITypes.UIText("test text").add_styling("n,l,u").nslow()
UIText.display()

# UI.add_content({
#     "text": "DETECTIVE PYTHON - THE GAME AND THE ADVENTURES of the new lord of the world so that's how it works !",
#     "styling": "newline | centered | upper | underline",
#     "slow": True,
#     "type": "sentence"
# })

# UI.add_content({
#     "text": "MY list :",
#     "styling":"upper | indented",
#     "slow":True,
#     "type":"list",
#     "list items": [
#         {
#             "text": "First item",
#             "styling": "upper",
#             "slow": True,
#             "type": "sentence"
#         },
#         {
#             "text": "second item",
#             "styling": "upper",
#             "slow": True,
#             "type": "sentence"
#         },
#         {
#             "text": "third item",
#             "styling": "upper",
#             "slow": True,
#             "type": "sentence"
#         }
#     ]
# })

# UI.add_content("u,i,c, nl|t|s|hola another line to be centered")
# UI.add_content("l,i,nl|t|s|Let's add a full paragraph and see how it looks when the library beautifies it and makes it more adequate for a good ui !")
# UI.add_content("u,i,nl|t|s|Let's add a full paragraph and see how it looks when the library beautifies it and makes it more adequate for a good ui !")
# UI.add_content("u,i,c,nl|t|s|Let's add a full paragraph and see how it looks when the library beautifies it and makes it more adequate for a good ui !")
# UI.display()
