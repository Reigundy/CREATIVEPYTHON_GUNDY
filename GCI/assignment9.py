import tkinter as tk
import random

root = tk.Tk()
root.title("i forgot my password")
root.geometry("400x300")

instructions = tk.Label(root, text="log on with your username and password", font=("Arial", 10))
instructions.pack()

# Frame for moving entries
form_frame = tk.Frame(root)
form_frame.pack(pady=20)

username_label = tk.Label(form_frame, text="Password:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(form_frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(form_frame, text="Username:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(form_frame, show="")
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(root, text="Submit?", font=("Courier", 14))
login_button.pack(pady=10)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

def scramble_form():
    # randomly move fields around
    username_label.grid(row=random.randint(0, 2), column=random.randint(0, 2))
    username_entry.grid(row=random.randint(0, 2), column=random.randint(0, 2))
    password_label.grid(row=random.randint(0, 2), column=random.randint(0, 2))
    password_entry.grid(row=random.randint(0, 2), column=random.randint(0, 2))
    # swap labels randomly
    if random.choice([True, False]):
        username_label.config(text="Username:")
        password_label.config(text="Password:")
    else:
        username_label.config(text="Password:")
        password_label.config(text="Username:")

    root.after(1500, scramble_form)

def fake_login():
    status_label.config(text="Wrong! Try again...", fg="red")
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

login_button.config(command=fake_login)

scramble_form()  # Start scrambling

root.mainloop()