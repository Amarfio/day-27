# import tkinter
from tkinter import *


def button_clicked():
    print("I get clicked")
    newText = input.get()
    my_label.config(text=newText)

window = Tk()
window.title("My First Gui Program")
window.minsize(width= 500, height=100)
window.config(padx=200, pady=200)



#Label
my_label= Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
# my_label.pack(side="left") #right, #bottom
# my_label.pack(expand="True")
# button = Button(text="Click me")
# button.pack()

#Button
button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

#new button
newButton = Button(text="New Button")
newButton.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)
print(input.get())


window.mainloop()