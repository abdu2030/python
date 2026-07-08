from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ----------------------------- PASSWORD GENERATOR ------------------------- #

def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ----------------------------- SAVE PASSWORD ----------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill all the fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ----------------------------- FIND PASSWORD ----------------------------- #

def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]

            messagebox.showinfo(
                title=website,
                message=f"Email: {email}\nPassword: {password}"
            )
        else:
            messagebox.showinfo(
                title="Error",
                message=f"No details for {website} exist."
            )


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e", padx=5, pady=5)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="e", padx=5, pady=5)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e", padx=5, pady=5)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, sticky="ew", padx=5, pady=5, ipady=3)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", padx=5, pady=5, ipady=3)
email_entry.insert(0, "abdulkerim@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew", padx=5, pady=5, ipady=3)

# Buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="ew", padx=5, pady=5, ipady=1)

generate_button = Button(text="Generate", width=10, command=generate_password)
generate_button.grid(column=2, row=3, sticky="ew", padx=5, pady=5, ipady=1)

add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew", padx=5, pady=5, ipady=1)

window.mainloop()