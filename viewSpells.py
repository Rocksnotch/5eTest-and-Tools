from tkinter import *
from tkinter import ttk
import fileHandler as fh

class viewSpells(Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("View Spells")
        self.state("zoomed")
        self.grid_columnconfigure((0, 1, 2), weight=1)

        label = Label(self, text="Spells", font=("Arial", 24)).grid(row=0, column=1)
        spells = fh.getSpells()
        
        def showSpellDetails(event):
            tree = event.widget
            selection = [tree.item(item)["text"] for item in tree.selection()]
    
    
            spells = fh.getSpells()
            for spell in spells["spells"]:
                if spell["name"] in selection[0]:
                    spellDetailsFrame = Frame(self)
                    spellDetailsFrame.grid(row=2, column=0, columnspan=3)
                    spellDetailsFrame.config(width=800, height=300, background="white")
                    spellDetailsFrame.grid_columnconfigure(0, minsize=800, weight=1)
                    
                    spellDetailsScrollbar = Scrollbar(spellDetailsFrame, orient="vertical")
                    spellDetailsScrollbar.grid(row=0, column=1, sticky=N+S, rowspan=2)
                    
                    # Spell Name
                    spellName = Label(spellDetailsFrame, text=spell["name"], font=("Arial", 16), background="white")
                    spellName.grid(row=0, column=0, sticky=W)
                    
                    # Spell Source
                    spellSource = Label(spellDetailsFrame, text="Source: " + spell["source"], font=("Arial", 10), background="white")
                    spellSource.grid(row=1, column=0, sticky=W, pady=(5,5))
                    
                    # Spell Level
                    if spell["level"] == "Cantrip":
                        spellLevel = Label(spellDetailsFrame, text=spell["school"] + " " + spell["level"], font=("Arial Italic", 10), background="white")
                    else:
                        if spell["ritual"] == True:
                            spellLevel = Label(spellDetailsFrame, text=spell["level"] + " "  + spell["school"] + " (ritual)", font=("Arial Italic", 10), background="white")
                        else:
                            spellLevel = Label(spellDetailsFrame, text=spell["level"] + " "  + spell["school"], font=("Arial Italic", 10), background="white")
                    spellLevel.grid(row=2, column=0, sticky=W, pady=(0,5))
                    
                    # Spell Casting Time
                    spelLCastTimeFrame = Frame(spellDetailsFrame, background="white")
                    spelLCastTimeFrame.grid(row=3, column=0, sticky=W)
                    spellCastTimeLabel = Label(spelLCastTimeFrame, text="Casting Time:", font=("Arial Bold", 10), background="white")
                    spellCastTimeLabel.pack(side=LEFT)
                    spellCastTimeActual = Label(spelLCastTimeFrame, text=spell["castTime"], font=("Arial", 10), background="white")
                    spellCastTimeActual.pack(side=LEFT)
                    
                    # Spell Range
                    spellRangeFrame = Frame(spellDetailsFrame, background="white")
                    spellRangeFrame.grid(row=4, column=0, sticky=W)
                    spellRangeLabel = Label(spellRangeFrame, text="Range:", font=("Arial Bold", 10), background="white")
                    spellRangeLabel.pack(side=LEFT)
                    spellRangeActual = Label(spellRangeFrame, text=spell["range"], font=("Arial", 10), background="white")
                    spellRangeActual.pack(side=LEFT)
                    
                    # Spell Components
                    spellComponentsFrame = Frame(spellDetailsFrame, background="white")
                    spellComponentsFrame.grid(row=5, column=0, sticky=W)
                    spellComponentsLabel = Label(spellComponentsFrame, text="Components:", font=("Arial Bold", 10), background="white")
                    spellComponentsLabel.pack(side=LEFT)
                    if spell["components"]["v"] == True:
                        if spell["components"]["s"] == True or spell["components"]["m"] != "":
                            spellComponentsV = Label(spellComponentsFrame, text="V,", font=("Arial", 10), background="white")
                        else:
                            spellComponentsV = Label(spellComponentsFrame, text="V", font=("Arial", 10), background="white")
                        spellComponentsV.pack(side=LEFT)
                    if spell["components"]["s"] == True:
                        if spell["components"]["m"] != "":
                            spellComponentsS = Label(spellComponentsFrame, text="S,", font=("Arial", 10), background="white")
                        else:
                            spellComponentsS = Label(spellComponentsFrame, text="S", font=("Arial", 10), background="white")
                        spellComponentsS.pack(side=LEFT)
                    if spell["components"]["m"] != "":
                        spellComponentsM = Label(spellComponentsFrame, text="M (" + spell["components"]["m"] + ")", font=("Arial", 10), background="white")
                        spellComponentsM.pack(side=LEFT)
                    
                    # Spell Duration
                    spellDurationFrame = Frame(spellDetailsFrame, background="white")
                    spellDurationFrame.grid(row=6, column=0, sticky=W)
                    spellDurationLabel = Label(spellDurationFrame, text="Duration:", font=("Arial Bold", 10), background="white")
                    spellDurationLabel.pack(side=LEFT)
                    spellDurationActual = Label(spellDurationFrame, text=spell["duration"], font=("Arial", 10), background="white")
                    spellDurationActual.pack(side=LEFT)
                    
                    # Spell Description
                    spellDescriptionFrame = Frame(spellDetailsFrame, background="white")
                    spellDescriptionFrame.grid(row=7, column=0, sticky=W)
                    spellDescriptionLabel = Label(spellDescriptionFrame, text=spell["description"].replace("\\n", "\n"), font=("Arial", 10), background="white", wraplength=800, justify=LEFT)
                    spellDescriptionLabel.pack(side=LEFT)

        spellTableFrame = Frame(self)
        spellTableFrame.grid(row=1, column=1)
        spellTable = ttk.Treeview(spellTableFrame, columns=("src", "lvl", "sch"))
        spellTable.heading("#0", text="Name", command=lambda: sortTreeviewColumn(spellTable, "#0", False))
        spellTable.heading("src", text="Source", command=lambda: sortTreeviewColumn(spellTable, "src", False))
        spellTable.heading("lvl", text="Level", command=lambda: sortTreeviewColumn(spellTable, "lvl", False))
        spellTable.heading("sch", text="School", command=lambda: sortTreeviewColumn(spellTable, "sch", False))
        spellTable.pack(side=LEFT)
        spellTable.bind("<<TreeviewSelect>>", showSpellDetails)

        scrollBar = Scrollbar(spellTableFrame, orient="vertical", command=spellTable.yview)
        scrollBar.pack(side=LEFT, fill="y")
        spellTable.configure(yscrollcommand=scrollBar.set)

        for spell in spells["spells"]:
            spellTable.insert("", "end", text=spell["name"], values=(spell["source"], spell["level"], spell["school"]))
        
        # Exit Button
        exitBtn = Button(self, text="Exit", font=("Arial", 12), width=8, command=self.destroy)
        exitBtn.grid(row=3, column=1)

        def sortTreeviewColumn(tv, col, reverse=False):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)
            tv.heading(col, command=lambda: sortTreeviewColumn(tv, col, not reverse))