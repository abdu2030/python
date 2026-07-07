from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
#----------------------------- PASSWORD GENERATOR -------------------------#

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


#----------------------------- SAVE PASSWORD -----------------------------#

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="please fill all the fields")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}"
                                                             f"\nPassword: {password} \nIs it ok to save??")
        if is_ok:
            with open("data.txt","a") as data_files:
                data_files.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:")
website.grid(column=0, row=1, sticky="e", padx=5, pady=5)

email = Label(text="Email/Username:")
email.grid(column=0, row=2, sticky="e", padx=5, pady=5)

password = Label(text="Password:")
password.grid(column=0, row=3, sticky="e", padx=5, pady=5)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew", padx=5, pady=5)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", padx=5, pady=5)
email_entry.insert(0,"abdulkerim@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew", padx=5, pady=5)

# Buttons
generate_button = Button(text="Generate", width=10,command=generate_password)
generate_button.grid(column=2, row=3, sticky="ew", padx=5, pady=5)

add_button = Button(text="Add",command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

window.mainloop()