from tkinter import *

#widgets = GUI elements: buttons, textboxes, labels, images
#windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window


window.geometry("420x420")
window.title("My first GUI program")
icon = PhotoImage(file='sky bg.png')
window.iconphoto(True,icon)
window.config(background='black')




window.mainloop() #place window on computer screen, listen for events
