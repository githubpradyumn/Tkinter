# #Creating input fields 
# from tkinter import *

# root = Tk()

# e = Entry(root)#,width=50,fg="black",bg="red",borderwidth=5)
# e.pack()
# e.insert(0," Enter your name: ")
# # e.get()

# def myClick():
#     hello = "Hello " + e.get()
#     myLable = Label(root,text=hello) #By the help of concatenation we can add text ( + " Hello Buddy \n How's your day ?")
#     myLable.pack()


# mybutton = Button(root, text = " click me\n if you want ", state="active",padx=5,pady=5, command=myClick, fg="red",bg="black")
# mybutton.pack()


# root.mainloop()

# import re

# def find_words_starting_with(text, letter):
#     # Case-insensitive search for words starting with the given letter
#     pattern = rf'\b{letter}\w*'
#     return re.findall(pattern, text, re.IGNORECASE)

# # Example usage
# text = "Hello, world! Hello, OpenAI. This is a test. Hello?"
# letter = 'h'
# print(find_words_starting_with(text, letter))


my_list = [1, 2, 3]
iterator = iter(my_list)
print(iterator)