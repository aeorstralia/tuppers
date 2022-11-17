import json
from os.path import join, basename
from glob import glob
from pathlib import Path

AvatarPrefix = "https://raw.githubusercontent.com/JamesHurburgh/Tuppers/main/"

# Initialise the object
aeorstraliaTuppers = {
    "tuppers": [],
    "groups": [
        {
            "id": 1,
            "name": "Aeorstralian NPCs"
        }
    ]
}

# Find the images
files = []
for ext in ('*.jpeg', '*.png', '*.jpg'):
   files.extend(glob(join("./", ext)))

# Add them to the file
for imageFile in files:
    filename = basename(imageFile)
    name = Path(imageFile).stem
    lowerCaseName = name.lower()
    kebabCase = lowerCaseName.replace(' ','-')
    newTupper = {
            "name": kebabCase,
            "avatar_url": f"{AvatarPrefix}{filename}",
            "brackets": [
                f"{kebabCase}:",
                ""
            ],
            "show_brackets": "false",
            "group_id": 1,
            "nick": name
        }
    aeorstraliaTuppers["tuppers"].append(newTupper)

# Write out the file
with open("aeorstraliaTuppers.json", "w") as outfile:
    outfile.write(json.dumps(aeorstraliaTuppers))