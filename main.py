from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox # must be imported seperately as it's just a module of code, not a class.
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    password_list = []
    password_list += ([choice(letters) for char in range(randint(8, 10))])
    password_list += ([choice(symbols) for char in range(randint(2, 4))])
    password_list += ([choice(numbers) for char in range(randint(2, 4))])
    shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    pyperclip.copy(password)
    return password

def password_fill():
    # Populates a generated password in the password field.
    password = pass_gen()
    password_input.delete(0, 'end')
    password_input.insert(0, f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    # save website, email, and password to .txt file with a new line between each entry and also clear fields except
    # for username.
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website:
            {"email" : username,
            "password" : password,
             }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error Notification: ", message="Please do not leave any fields empty. ")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered\n"
                                                              f"\nEmail: "
                                                              f" {username} "
                                                              f"\nPasswor"
                                                      f"d: {password} \n\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as dp:
                    # Read old data
                    data = json.load(dp)
                    # Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError: # If json file is empty or does not exist.
                with open("data.json", "w") as dp:
                    json.dump(new_data, dp, indent=4)
            else:
                with open("data.json", "w") as dp:
                    json.dump(data, dp, indent=4)
            finally:
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')

# ---------------------------- SEARCH ------------------------------- #

def find_password():
    website = website_input.get().title()
    try:
        with open("data.json", "r") as dp:
            pass_data = json.load(dp)
            try:
                messagebox.showinfo(f"Website: {website}\n\n", message=f"Email/Username: "
                                                                  f"{pass_data[website]['email']}\n"
                                                                  f"Password: {pass_data[website]['password']}")
            except KeyError:
                messagebox.showinfo(title="Error", message=f"No details for the website or program exist. ")

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas image and dimensions
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Website labels & entry
website_label = Label(text="Website/Program:")
website_label.grid(row=1, column=0)
website_input = Entry(width=21)
website_input.grid(column=1, row=1, sticky="EW")
website_input.focus()


# Username labels & entry
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
username_input.insert(0, "michael@gmail.com")


# Password labels & entry
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")


# Buttons
generate_password_b = Button(text="Generate Password", command=password_fill)
generate_password_b.grid(column=2, row=3, sticky="EW")
submit_info = Button(text="Add", width=36, command=save)
submit_info.grid(column=1, row=4, columnspan=2, stick="EW")
search_b = Button(text="Search", width=15, command=find_password)
search_b.grid(column=2, row=1, sticky="EW")


window.mainloop()