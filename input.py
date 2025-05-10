#entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()
    print("Hello "+username)

def delete():
    entry.delete(0,END) #delete the line of text

def backspace():
    entry.delete(len(entry.get())-1,END) #delete last character

window = Tk()

submit = Button(window, text="Submit", command=submit)
submit.pack(side = RIGHT)

delete = Button(window, text="Delete", command=delete)
delete.pack(side = RIGHT)

backspace = Button(window, text="Backspace",command=backspace)
backspace.pack(side = RIGHT)

entry = Entry()
entry.config(font=('ink free', 50))
entry.config(bg='#111111')
entry.config(fg='#00ff00')
#entry.config(state=DISABLED)
entry.insert(0, 'RIPON')
entry.config(show='*')#works perfect for password

entry.pack()
window.mainloop()


