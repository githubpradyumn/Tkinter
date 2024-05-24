from tkinter import *

root = Tk()
#creating a Label Widget
myLable1 = Label(root, text="Hello World!")
myLable2= Label(root, text="My name is Pradyumn Pratap Singh")

#shoving it onto the screen
myLable1.grid(row=0,column=0)
myLable2.grid(row=2,column=8)


#another way of creating and shoving
# myLable1 = Label(root, text="Hello World!").grid(row=0,column=0)
# myLable2= Label(root, text="My name is Pradyumn Pratap Singh").grid(row=2,column=8)



root.mainloop()