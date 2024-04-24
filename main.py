from tkinter import *
import fileHandler as fh
import addSpells as add
import viewSpells as view

# Global variables

# Function to save the file and exit the program
def saveExit():
    fh.saveFile(spells)
    root.destroy()

# Main function
if __name__ == '__main__':

    # Load existing file
    spells = fh.loadFile()
    fh.loadedFile = spells

    # Create the main window
    root = Tk()
    root.title('D&D Spellbook Database')
    root.state('zoomed')

    # Top Menu Label
    Label(root, text='D&D Spellbook Database', font=('Arial', 24)).pack()

    # Button to add a new spell, which opens the addSpell window
    addBtn = Button(root, text='Add New Spell', font=('Arial', 12), width=12, command=add.addSpell).pack(side=TOP, pady=(50,0))
    
    # Button to view all spells
    viewBtn = Button(root, text='View All Spells', font=('Arial', 12), width=12, command=view.viewSpells).pack(side=TOP)

    # Button to exit program
    exitBtn = Button(root, text='Exit', font=('Arial', 12), width=12, command=saveExit).pack(side=TOP)

    root.mainloop()