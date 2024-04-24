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

        spellTableFrame = Frame(self)
        spellTableFrame.grid(row=1, column=1)
        spellTable = ttk.Treeview(spellTableFrame, columns=("src", "lvl", "sch"))
        spellTable.heading("#0", text="Name", command=lambda: sortTreeviewColumn(spellTable, "#0", False))
        spellTable.heading("src", text="Source", command=lambda: sortTreeviewColumn(spellTable, "src", False))
        spellTable.heading("lvl", text="Level", command=lambda: sortTreeviewColumn(spellTable, "lvl", False))
        spellTable.heading("sch", text="School", command=lambda: sortTreeviewColumn(spellTable, "sch", False))
        spellTable.pack(side=LEFT)

        scrollBar = Scrollbar(spellTableFrame, orient="vertical", command=spellTable.yview)
        scrollBar.pack(side=LEFT, fill="y")
        spellTable.configure(yscrollcommand=scrollBar.set)

        for spell in spells["spells"]:
            spellTable.insert("", "end", text=spell["name"], values=(spell["source"], spell["level"], spell["school"]))

        exitBtn = Button(self, text="Exit", font=("Arial", 12), width=8, command=self.destroy).grid(row=2, column=1)

        def sortTreeviewColumn(tv, col, reverse=False):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)
            tv.heading(col, command=lambda: sortTreeviewColumn(tv, col, not reverse))