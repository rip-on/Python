#button = you click it, then it does stuff

from tkinter import *
count = 0
def click():
    global count
    count+=1
    #print(count)
    label.config(text=count)
window = Tk()
button = Button(window,
                text="Click me!!!")
button.config(command=click)#Performs call back of function
button.pack()
button.config(font=('Ink Free',50,'bold'))
button.config(bg='orange')
button.config(fg='yellow')
button.config(activebackground='#FF0000')
button.config(activeforeground='yellow')
image = PhotoImage(file='pointer.png')
button.config(image=image)
button.config(compound='top')
button.config(state=ACTIVE) #disabled button(ACTIVE/DISABLED)
label=Label(window,text=count)
label.config(font=('Monospace',50))
label.pack()
window.mainloop()
