# Handles the file operations for the program. This includes loading the file and saving the file.
import json

loadedFile = None

def loadFile():
    try:
        with open("spells.json", "r") as file:
            print("File found. Loaded file.")
            spells = json.load(file)
    except FileNotFoundError:
        with open("spells.json", "w") as file:
            print("File not found. Created new file.")
            file.write(json.dumps({"spells": []}, indent=4))
            spells = {"spells": []}
    return spells

def saveFile(spells):
    with open("spells.json", "w") as file:
        print("Saved file.")
        file.write(json.dumps(spells, indent=4))
    return

def getSpells():
    return loadedFile