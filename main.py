from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


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
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_btn = Button(text="Generate Password", width=14)
generate_password_btn.grid(row=3, column=2)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

# ---------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window.mainloop()
