import customtkinter as ctk
import Logic
import pandas as pd

def prev_paths():
    with open("paths.txt", "r") as file:
        paths = file.readlines()
        paths = [path.strip() for path in paths]
        return paths

def updateEntry(value):
    entry_field.delete(0, ctk.END)
    entry_field.insert(0, value)

window = ctk.CTk()

window.title('Choose Folder')
entry_field = ctk.CTkEntry(window, placeholder_text='Enter path', width=300)
entry_field.pack(fill='both', expand=True)

options = prev_paths()

button = ctk.CTkButton(window, width=300, text='Save', command= lambda: Logic.logic(entry_field.get(), options))
button.pack(fill='both', expand=True)


selected = ctk.StringVar()
dropdown = ctk.CTkComboBox(window, values=options, command= updateEntry)
dropdown.set('Prev Paths')

dropdown.pack(fill='both', expand = True)
window.mainloop()