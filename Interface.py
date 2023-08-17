import customtkinter as ctk
import Logic
import pandas as pd
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

def prev_paths():
    # Use the absolute path to the file
    paths_file = os.path.join(script_dir, "paths.txt")
    
    with open(paths_file, "r") as file:
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

button = ctk.CTkButton(window, width=300, text='Save', command= lambda: Logic.logic(entry_field.get(), options, script_dir))
button.pack(fill='both', expand=True)


selected = ctk.StringVar()
dropdown = ctk.CTkComboBox(window, values=options, command= updateEntry)
dropdown.set('Prev Paths')

dropdown.pack(fill='both', expand = True)
window.mainloop()
