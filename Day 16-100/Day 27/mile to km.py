from tkinter import *

def mile_km():
    miles = float(input_field.get())
    km = miles * 1.609
    result_label.config(text=f"{km:.4f}")

window = Tk()
window.title("Mile to km")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

input_field = Entry(width=10)
input_field.pack()

label = Label(text="is equal to")
label.pack()

result_label = Label(text="0")
result_label.pack()

button = Button(text="Calculate", command=mile_km)
button.pack()

window.mainloop()
