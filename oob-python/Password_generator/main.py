import json
from  tkinter import *
from tkinter import messagebox
import random
import  pyperclip

# ---------------------------- FIND PASSWORD ------------------------------- #

def search_pass():
    website = website_entry.get().lower()
    try:
        with open("password.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found")
    else:
        website_lower = {key.lower(): value for key, value in data.items()}
        if website in website_lower:
            email = website_lower[website]["email"]
            password = website_lower[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

        else:
            messagebox.showinfo(title="Error", message="Password not found for website")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password_gen = "".join(password_list)

    password_entry.insert(0, password_gen)
    pyperclip.copy(password_gen)


    print(f"Your password is: {password_gen}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {"email": email,
                  "password": password,
                  }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="you left some fields empty")
    else:
        try:
            with open("password.json", "r") as file:
                #Read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("password.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            #Update old data with new data
            data.update(new_data)

            with open("password.json", "w") as file:
                #Save the updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        print("Password Saved")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@abc.com")
password_entry = Entry(width=35)
password_entry.grid(row=3,column=1)

#Buttons:
search_button = Button(text="search", command=search_pass, width=15)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()