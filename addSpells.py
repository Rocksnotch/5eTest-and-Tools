from tkinter import *
import fileHandler as fh

levels = ["Cantrip", "1st-Level", "2nd-Level", "3rd-Level", "4th-Level", "5th-Level", "6th-Level", "7th-Level", "8th-Level", "9th-Level"]

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

class addSpell(Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Add Spell")
        self.state("zoomed")
        self.grid_columnconfigure((0, 1, 2), weight=1)

        addSpell.var1 = StringVar(self)
        addSpell.var1.set("Cantrip")

        addSpell.var2 = StringVar(self)
        addSpell.var2.set("Abjuration")

        addSpell.var3 = BooleanVar(self)
        addSpell.var3.set('0')

        addSpell.var4 = BooleanVar(self)
        addSpell.var4.set('0')

        addSpell.var5 = BooleanVar(self)
        addSpell.var5.set('0')
    
        mainLabel = Label(self, text="Add Spell", font=("Arial", 24)).grid(row=0, column=1)

        # Frame for Spell Name and appropriate widgets
        spellNameFrame = Frame(self)
        spellNameFrame.grid(row=1, column=1)
        spellNameLabel = Label(spellNameFrame, text="Spell Name:").pack(side=LEFT)
        spellNameEntry = Entry(spellNameFrame).pack(side=LEFT)

        # Frame for Spell Source and appropriate widgets
        spellSourceFrame = Frame(self)
        spellSourceFrame.grid(row=2, column=1)
        spellSourceLabel = Label(spellSourceFrame, text="Spell Source:").pack(side=LEFT)
        spellSourceEntry = Entry(spellSourceFrame).pack(side=LEFT)

        # Frame for Spell Level / Ritual checkbox and appropriate widgets
        spellLevelFrame = Frame(self)
        spellLevelFrame.grid(row=3, column=1)
        spellLevelLabel = Label(spellLevelFrame, text="Spell Level:").pack(side=LEFT)
        spellLevelOption = OptionMenu(spellLevelFrame, addSpell.var1, StringVar(), *levels).pack(side=LEFT)
        spellRitualCheck = Checkbutton(spellLevelFrame, variable = addSpell.var3, text="Ritual?", onvalue=True, offvalue=False).pack(side=LEFT)

        # Frame for Spell School and appropriate widgets
        spellSchoolFrame = Frame(self)
        spellSchoolFrame.grid(row=4, column=1)
        spellSchoolLabel = Label(spellSchoolFrame, text="Spell School:").pack(side=LEFT)
        spellSchoolOption = OptionMenu(spellSchoolFrame, addSpell.var2, StringVar(), "Abjuration", "Conjuration", "Divination", "Enchantment", "Evocation", "Illusion", "Necromancy", "Transmutation").pack(side=LEFT)

        # Frame for Spell Casting Time and appropriate widgets
        spellCastTimeFrame = Frame(self)
        spellCastTimeFrame.grid(row=5, column=1)
        spellCastTimeLabel = Label(spellCastTimeFrame, text="Casting Time:").pack(side=LEFT)
        spellCastTimeEntry = Entry(spellCastTimeFrame).pack(side=LEFT)

        # Frame for Spell Range and appropriate widgets
        spellRangeFrame = Frame(self)
        spellRangeFrame.grid(row=6, column=1)
        spellRangeLabel = Label(spellRangeFrame, text="Range:").pack(side=LEFT)
        spellRangeEntry = Entry(spellRangeFrame).pack(side=LEFT)

        # Frame for Spell Components and appropriate widgets
        spellComponentsFrame = Frame(self)
        spellComponentsFrame.grid(row=7, column=1)
        spellComponentsLabel = Label(spellComponentsFrame, text="Verbal Component? ").pack(side=LEFT)
        spellComponentsVCheck = Checkbutton(spellComponentsFrame, variable = addSpell.var4, onvalue=True, offvalue=False).pack(side=LEFT)
        spellComponentsLabel = Label(spellComponentsFrame, text="Somatic Component? ").pack(side=LEFT)
        spellComponentsSCheck = Checkbutton(spellComponentsFrame, variable = addSpell.var5, onvalue=True, offvalue=False).pack(side=LEFT)
        spellComponentsLabel = Label(spellComponentsFrame, text="Material Component: ").pack(side=LEFT)
        spellComponentsMEntry = Entry(spellComponentsFrame).pack(side=LEFT)

        # Frame for Spell Duration and appropriate widgets
        spellDurationFrame = Frame(self)
        spellDurationFrame.grid(row=8, column=1)
        spellDurationLabel = Label(spellDurationFrame, text="Duration:").pack(side=LEFT)
        spellDurationEntry = Entry(spellDurationFrame).pack(side=LEFT)

        # Frame for Spell Description and appropriate widgets
        spellDescriptionFrame = Frame(self)
        spellDescriptionFrame.grid(row=9, column=1)
        spellDescriptionLabel = Label(spellDescriptionFrame, text="Description:").pack(side=LEFT)
        spellDescriptionEntry = Text(spellDescriptionFrame, width=120, height=10)
        spellDescriptionEntry.pack(side=LEFT)
        scrollY = Scrollbar(spellDescriptionFrame, orient=VERTICAL, command=spellDescriptionEntry.yview)
        scrollY.pack(side=LEFT, fill=Y)
        spellDescriptionEntry['yscrollcommand'] = scrollY.set
        
    
        # Frame for Higher Levels Description and appropriate widgets
        spellHigherLevelsFrame = Frame(self)
        spellHigherLevelsFrame.grid(row=10, column=1)
        spellHigherLevelsLabel = Label(spellHigherLevelsFrame, text="Higher Levels Description:").pack(side=LEFT)
        spellHigherLevelsEntry = Text(spellHigherLevelsFrame, width=100, height=5).pack(side=LEFT)

        # Frame for Spell Classes and appropriate widgets
        spellClassesFrame = Frame(self)
        spellClassesFrame.grid(row=11, column=1)
        spellClassesLabel = Label(spellClassesFrame, text="Classes (Comma Separated):").pack(side=LEFT)
        spellClassesEntry = Entry(spellClassesFrame, width=50).pack(side=LEFT)

        # Frame for Buttons
        spellButtonFrame = Frame(self)
        spellButtonFrame.grid(row=12, column=1)
        addSpellBtn = Button(spellButtonFrame, text="Add Spell", font=("Arial", 12), width=8, command=self.createEntry).pack(side=LEFT)
        clearBtn = Button(spellButtonFrame, text="Clear", font=("Arial", 12), width=8, command=self.clearFields).pack(side=LEFT)
        exitBtn = Button(spellButtonFrame, text="Exit", font=("Arial", 12), width=8, command=self.destroy).pack(side=LEFT)


    # Function to clear all fields in the window
    def clearFields(args):
        addSpell.winfo_children(args)[1].winfo_children()[1].delete(0, END)
        addSpell.winfo_children(args)[2].winfo_children()[1].delete(0, END)
        addSpell.var1.set("Cantrip")
        addSpell.var2.set("Abjuration")
        addSpell.var3.set('0')
        addSpell.winfo_children(args)[5].winfo_children()[1].delete(0, END)
        addSpell.winfo_children(args)[6].winfo_children()[1].delete(0, END)
        addSpell.var4.set('0')
        addSpell.var5.set('0')
        addSpell.winfo_children(args)[7].winfo_children()[5].delete(0, END)
        addSpell.winfo_children(args)[8].winfo_children()[1].delete(0, END)
        addSpell.winfo_children(args)[9].winfo_children()[1].delete("1.0", END)
        addSpell.winfo_children(args)[10].winfo_children()[1].delete("1.0", END)
        addSpell.winfo_children(args)[11].winfo_children()[1].delete(0, END)

    # Function to create a new entry in the json file, takes in window as argument
    def createEntry(args):
        try:
            spells = fh.getSpells()
            newEntry = entry.copy()
            newEntry["name"] = addSpell.winfo_children(args)[1].winfo_children()[1].get()
            newEntry["source"] = addSpell.winfo_children(args)[2].winfo_children()[1].get()
            newEntry["level"] =  addSpell.var1.get()
            newEntry["school"] = addSpell.var2.get()
            newEntry["ritual"] = addSpell.var3.get()
            newEntry["castTime"] = addSpell.winfo_children(args)[5].winfo_children()[1].get()
            newEntry["range"] = addSpell.winfo_children(args)[6].winfo_children()[1].get()
            newEntry["components"]["v"] = addSpell.var4.get()
            newEntry["components"]["s"] = addSpell.var5.get()
            newEntry["components"]["m"] = addSpell.winfo_children(args)[7].winfo_children()[5].get()
            newEntry["duration"] = addSpell.winfo_children(args)[8].winfo_children()[1].get()
            newEntry["description"] = addSpell.winfo_children(args)[9].winfo_children()[1].get("1.0", "end-1c")
            newEntry["higherLevels"] = addSpell.winfo_children(args)[10].winfo_children()[1].get("1.0", "end-1c")
            newEntry["classes"] = addSpell.winfo_children(args)[11].winfo_children()[1].get().split(",")
            spells["spells"].append(newEntry)
            top = Toplevel(args)
            top.title("Success!")
            top.geometry("300x100")
            topLabel = Label(top, text="Spell added to list successfully!").pack()
            topButton = Button(top, text="OK", command=top.destroy).pack()
            addSpell.clearFields(args)
        except:
            top = Toplevel(args)
            top.title("Error")
            top.geometry("300x100")
            topLabel = Label(top, text="Error: Unable to add spell for unknown reason.").pack()
            topButton = Button(top, text="OK", command=top.destroy).pack()