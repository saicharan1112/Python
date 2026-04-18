from tkinter import *

# Create window
root = Tk()
root.title("Registration Form")
root.geometry("300x250")

# Labels and Entry fields
Label(root, text="Name").pack()
name = Entry(root)
name.pack()

Label(root, text="Email").pack()
email = Entry(root)
email.pack()

Label(root, text="Password").pack()
password = Entry(root, show="*")
password.pack()

Label(root, text="Gender").pack()

g = StringVar()
Radiobutton(root, text="Male", variable=g, value="Male").pack()
Radiobutton(root, text="Female", variable=g, value="Female").pack()

# Button
Button(root, text="Register").pack()

# Run window
root.mainloop()
