import json

# Dictionary template for each entry in the json file, with each value being a variable to enter later
entry = {
    "name": "",
    "source": "",
    "level": 0,
    "school": "",
    "ritual": False,
    "castTime": "",
    "range": "",
    "components": {
        "v": False,
        "s": False,
        "m": ""
    },
    "duration": "",
    "description": "",
    "higherLevels": "",
    "classes": []
}

# Dictionary template for new json file
newFile = {
    "spells": [
        
    ]
}

levels = ["Cantrip", "1st-Level", "2nd-Level", "3rd-Level", "4th-Level", "5th-Level", "6th-Level", "7th-Level", "8th-Level", "9th-Level"]

# Load json file, or create it if it doesn't exist. Either way, save to variable loadedFile
def loadFile():
    try:
        with open("spells.json", "r") as file:
            print("File found. Loaded file.")
            loadedFile = json.load(file)
                    
    except FileNotFoundError:
        with open("spells.json", "w") as file:
            print("File not found. Created new file.")
            file.write(json.dumps(newFile, indent=4))
        loadedFile = newFile
    return loadedFile

def viewSpellInfo():
    print("\033[H\033[J")
    print("+---[View Spell Info]---+")
    spellName = input("Enter Name of Spell: ")
    print("\033[H\033[J")
    for spell in loadedFile["spells"]:
        if spell["name"].lower() == spellName.lower():
            print(f"\033[H\033[J")
            print(f"{spell['name']}")
            print(f"\nSource: {spell['source']}")
            if spell['level'] == 0:
                print(f"\n{spell['school']} {levels[spell["level"]]}")
            else:
                print(f"\n{levels[spell["level"]]} {spell['school']}")
            if spell['ritual']:
                print(" (Ritual)")
            print(f"\nCasting Time: {spell['castTime']}")
            print(f"Range: {spell['range']}")
            
            # Print out components, but only if they exist
            print("Components: ", end="")

            if spell['components']['v']:
                print("V", end="")
                if spell['components']['s'] or spell['components']['m']:
                    print(", ", end="")
                else:
                    print("", end="\n")

            if spell['components']['s']:
                print("S", end="")
                if spell['components']['m'] != "":
                    print(", ", end="")
                else:
                    print("", end="\n")

            if spell['components']['m'] != "":
                print(f"M ({spell['components']['m']})")

            print(f"Duration: {spell['duration']}")
            
            print(f"\nDescription: {spell['description'].replace("\\n", "\n")}")
            print(f"\nHigher Levels: {spell['higherLevels']}")
            print(f"\nClasses: {', '.join(spell['classes'])}")
            input("\n\nPress Enter to continue...")
            print("\033[H\033[J")
            return
    print("Spell not found. Returning to main menu...")
    input("Press Enter to continue...")
    print("\033[H\033[J")

def createEntry():
    newEntry = entry.copy()
    newEntry["name"] = input("Enter Name of Spell: ")
    for spell in loadedFile["spells"]:
        if spell["name"].lower() == newEntry["name"].lower():
            print("Spell already exists. Returning to main menu...")
            input("Press Enter to continue...")
            return
    newEntry["source"] = input("Enter Source book of Spell (Abbreviation): ")
    newEntry["level"] = int(input("Enter Level of Spell: "))
    newEntry["school"] = input("Enter School of Spell: ")
    newEntry["ritual"] = input("Is this spell a ritual? (y/n): ").lower()
    if newEntry["ritual"] == "y":
        newEntry["ritual"] = True
    else:
        newEntry["ritual"] = False
    newEntry["castTime"] = input("Enter Casting Time: ")
    newEntry["range"] = input("Enter Range of Spell: ")
    newEntry["components"]["v"] = input("Does this spell require Verbal components? (y/n): ").lower()
    if newEntry["components"]["v"] == "y":
        newEntry["components"]["v"] = True
    else:
        newEntry["components"]["v"] = False
    newEntry["components"]["s"] = input("Does this spell require Somatic components? (y/n): ").lower()
    if newEntry["components"]["s"] == "y":
        newEntry["components"]["s"] = True
    else:
        newEntry["components"]["s"] = False
    newEntry["components"]["m"] = input("Enter Material components (if any): ")
    newEntry["duration"] = input("Enter Duration of Spell: ")
    newEntry["description"] = input("Enter Description of Spell: ")
    newEntry["higherLevels"] = input("Enter Higher Levels description (if any): ")
    newEntry["classes"] = input("Enter Classes that can use this spell (comma separated): ").split(",")
    # Add new entry to loadedFile
    loadedFile["spells"].append(newEntry)



# Main program loop
# Load file
loadedFile = loadFile()
input("Press Enter to continue...")
print("\033[H\033[J")

# Run main loop until user exits

while True:
    # Main Menu Options
    print("+---[Main Menu]---+")
    print("| 1: Add Spell    |")
    print("| 2: View List    |")
    print("| 3: View Spell   |")
    print("| 4: Exit         |")
    print("+-----------------+")
    userChoice = input("Enter Choice: ")
    
    match userChoice:
        case "1":
            # Add Spell
            print("\033[H\033[J")
            # Create new entry
            createEntry()
            print("\033[H\033[J")
            
        case "2":
            # View Spells
            print("\033[H\033[J")
            print("+---[View Spells]---+")
            for spell in loadedFile["spells"]:
                print(f"{spell['name']} ({spell['source']}): {spell['level']} {spell['school']} Spell")
            input("(Press Enter to continue...)")
            print("\033[H\033[J")
        case "3":
            # View Spell Info
            viewSpellInfo()
        case "4":
            with open("spells.json", "w") as file:
                file.write(json.dumps(loadedFile, indent=4))
            print("\033[H\033[J")
            break
        case _:
            print("Invalid Choice. Please try again.")
            input("(Press Enter to continue...)")
            print("\033[H\033[J")