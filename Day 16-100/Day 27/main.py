from tkinter import *

def button_clicked():
    # print("clicked")
    my_label.config(text="i got clicked")

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

#Label
my_label = Label(text="i am me", font=("Arial", 24))
my_label.config(text="New Text")
#my_label.pack()
# my_label.place(x=0,y=0)
my_label.grid(column=0,row=0)

#button
button = Button(text="click me", command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

button2 = Button(text="haha", )
button2.grid(column=2,row=0)

#entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=2,row=2)


window.mainloop()
