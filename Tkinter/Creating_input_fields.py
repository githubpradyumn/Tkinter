#Creating input fields 
from tkinter import *

root = Tk()

e = Entry(root)#,width=50,fg="black",bg="red",borderwidth=5)
e.pack()
e.insert(0," Enter your name: ")
# e.get()

def myClick():
    hello = "Hello " + e.get()
    myLable = Label(root,text=hello) #By the help of concatenation we can add text ( + " Hello Buddy \n How's your day ?")
    myLable.pack()


mybutton = Button(root, text = " click me\n if you want ", state="active",padx=5,pady=5, command=myClick, fg="red",bg="black")
mybutton.pack()


root.mainloop()
