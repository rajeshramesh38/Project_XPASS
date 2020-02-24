import json
from tkinter import *

import mapper
import splitnencode

pattern_file = open("patterns.json", "r")
patterns = json.load(pattern_file)


def final_pass(pass_str):
    t = splitnencode.encoder(pass_str)
    popup = Tk()
    popup.wm_title("Generated Password")
    Label(popup, text=str(t), font=("Helvetica", 12), width=20).pack()
    Button(popup, text="OK", command=popup.destroy, width=20).pack()
    popup.mainloop()


def prints():
    pwd = e1.get()
    encoded_form = mapper.mapping(pwd, patterns['0'])
    root = Tk()
    root.title("Mapped Values")
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    mylist = Listbox(root, yscrollcommand=scrollbar.set, width=100)
    for line in range(len(encoded_form)):
        mylist.insert(END, str("Value of " + pwd[line].upper() + " : " + encoded_form[line]))
    mylist.pack(side=TOP)
    mylist.configure(width=50)
    scrollbar.config(command=mylist.yview)
    final_pass(encoded_form)
    mainloop()


master = Tk()
master.title("X-Pass")
Label(master, text="Getting User Password").grid(row=0)
e1 = Entry(master, width=25)
e1.grid(row=0, column=1)
button1 = Button(master, text="Generate Strong Password", command=prints)
button1.grid(row=1, pady=5)
master.mainloop()
