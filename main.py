from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
from zlib import DEF_BUF_SIZE
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
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
    Password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = Website_entry.get().title()
    email = Email_entry.get()
    password = Password_entry.get().title()
    new_data = {web : {
        "email": email,
        "password" : password
    }}

# SAVING DATA IN TXT FILE
    if len(web)==0 or len(email)==0 or len(password) ==0:
        messagebox.showinfo(title="oops",message="dont leave any coloumn empty")
    else:
        a = messagebox.askokcancel(title="title",message=f"You Entered\n{web}\n{password}")

        if a:
            with open(file="E:/project day 22 to/day 29 password/data.txt",mode="a") as file:
                file.write(f"{web}  |  {email}  |  {password}\n")
                Website_entry.delete(0,END)
                Password_entry.delete(0,END)

#SAVING FILE IN JSON FILE
            try:
                with open("E:/project day 22 to/day 29 password/data.json",mode='r') as data_file:   
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("E:/project day 22 to/day 29 password/data.json",mode='w') as data_file:
                    json.dump(new_data , data_file , indent=4)
            else:
                data.update(new_data)
                with open("E:/project day 22 to/day 29 password/data.json",mode='w') as data_file:
                    json.dump(data , data_file , indent=4)           

# ---------------------------- FIND PASSWORD ------------------------------- #   

def find_password():
    web = Website_entry.get().title()
    try:
        with open("E:/project day 22 to/day 29 password/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if web in data:
            email = data[web]["email"]
            password = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web} exists.")

    
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password")
window.config(padx=30,pady=30)

canvas = Canvas(width=200,height=200,highlightthickness=0)
my_pass_logo = PhotoImage(file="E:\project day 22 to\day 29 password/logo.png")
canvas.create_image(100,100,image=my_pass_logo)
canvas.grid(row=0,column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

#Entries
Website_entry = Entry(width=35)
Website_entry.focus()
Website_entry.grid(row=1,column=1,columnspan=2)

Email_entry = Entry(width=35)
Email_entry.insert(0,"chhillarkaran2310@gmail.com")
Email_entry.grid(row=2,column=1,columnspan=2)

Password_entry = Entry(width=35)
Password_entry.grid(row=3,column=1,columnspan=2)

#buttons
search_button = Button(text="Search",width=15,command=find_password)
search_button.grid(row=1,column=2)

generate_password_button = Button(text="Generate Password",width=15,command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button = Button(text="ADD",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()