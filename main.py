from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

username_input = Entry(width=35)
username_input.grid(column=1, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3, columnspan=1)

generate_password_b = Button(text="Generate Password")
generate_password_b.grid(column=2, row=3)

submit_info = Button(text="Add")
submit_info.grid(column=1, row=4)




window.mainloop()