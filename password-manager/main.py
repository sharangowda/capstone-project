from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def random_pass():
    let = [ch for ch in random.choices(letters, k=5)]
    num = [num for num in random.choices(numbers, k=5)]
    sym = [sym for sym in random.choices(symbols, k=5)]
    pas = let + num + sym
    new = ''.join(pas)
    password_entry.insert(0, new)
    pyperclip.copy(new)



def save_data():
    passw = {website_entry.get(): {'email': email_entry.get(),
                                   'password': password_entry.get()}}
    with open('passwords.json', 'r') as password:
        data = json.load(password)
        data.update(passw)
    with open('passwords.json', 'w') as password1:
        json.dump(data, password1, indent=4)
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    messagebox.showinfo(message="Password saved.")


window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(
    file="password-manager-(finish search option later)\logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_title = Label(text='Website:')
website_title.grid(row=1, column=0)

website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)

email_title = Label(text='Username/Email:')
email_title.grid(row=2, column=0)

email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)

password_title = Label(text='Password:')
password_title.grid(row=3, column=0)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

password_button = Button(text='Generate password',
                         width=14, command=random_pass)
password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=42, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
