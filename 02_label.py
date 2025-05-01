#label = an area widget that holds text and/or an image within a window


from tkinter import *
window = Tk()
photo = PhotoImage(file='hck.png')
label = Label(window,
              text="Jahid Hasan",
              font=('tahoma',50,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED, #sunken
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="bottom")
label.pack()
window.title("My Name")
window.geometry('1120x820')
window.mainloop()