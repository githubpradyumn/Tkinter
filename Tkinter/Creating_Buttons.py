from tkinter import *

root = Tk()

def myClick():
    myLable = Label(root,text="Look what i have done in this\nJust click the button")
    myLable.pack()


mybutton = Button(root, text = "Click me", state="active",padx=10,pady=5, command=myClick, fg="red",bg="black")
mybutton.pack()


root.mainloop()