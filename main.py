from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

import pyperclip


# password generator

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) > 0 or len(password) > 0:
        messagebox.showinfo(title='Missing', message="Enter both website and password")

        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email}"
                                               f"\nPassword: {password} \n it it ok to save")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f' {website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showerror(title='Missing', message="Enter both email and password")


# -------------------------------------

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logoImg = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logoImg)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'rahimiehsan1997@gmail.com')
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_btn = Button(text="Generate Password", width=14, command=generate_password)
generate_password_btn.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# ---------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window.mainloop()
