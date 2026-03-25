import tkinter as tk

def submit():
    username = user_entry.get()
    password = pass_entry.get()
    autograph = auto_entry.get()

    result.config(text="👋 Welcome " + username + " 😊\n✍ Autograph: " + autograph)

window = tk.Tk()
window.title("Welcome Form")
window.geometry("350x320")
window.configure(bg="#fff2cc")

# Title
title = tk.Label(window, text="🌟 welcome to giet 🌟",
                 font=("Arial",16,"bold"),
                 bg="#fff2cc",
                 fg="BLACK")
title.pack(pady=10)

# Username
user_label = tk.Label(window, text="🧑 Username:",
                      font=("Arial",12),
                      bg="#fff2cc")
user_label.pack()

user_entry = tk.Entry(window, font=("Arial",12))
user_entry.pack(pady=5)

# Password
pass_label = tk.Label(window, text="🔐 Password:",
                      font=("Arial",12),
                      bg="#fff2cc")
pass_label.pack()

pass_entry = tk.Entry(window, show="*", font=("Arial",12))
pass_entry.pack(pady=5)

# Autograph
auto_label = tk.Label(window, text="✍ Autograph:",
                      font=("Arial",12),
                      bg="#fff2cc")
auto_label.pack()

auto_entry = tk.Entry(window, font=("Arial",12))
auto_entry.pack(pady=5)

# Submit Button
btn = tk.Button(window, text="🚀 Submit",
                font=("Arial",12,"bold"),
                bg="green",
                fg="white",
                command=submit)
btn.pack(pady=10)

# Result
result = tk.Label(window, text="",
                  font=("Arial",12),
                  bg="#5A59081A")
result.pack(pady=10)

window.mainloop()