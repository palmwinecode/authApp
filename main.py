import pathlib

import tkinter as tk

from tkinter import messagebox

from PIL import ImageTk

class Login:
    
    def __init__(self, root) -> None:
        # Create instance variable
        self.root = root
        
        # Background image
        # Dynamically determine image path
        img_file_name = "background.jpg"
        current_dir = pathlib.Path(__file__).parent.resolve()
        img_path = current_dir.joinpath(img_file_name)

        # Add background image to window
        self.bg = ImageTk.PhotoImage(file=img_path)
        self.bg_image = tk.Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        login_frame = tk.Frame(self.root, bg="white")
        login_frame.place(x=300, y=150, width=500, height=400)

        # Title and subtitle
        title = tk.Label(login_frame, text="Login", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90, y=30)
        subtitle = tk.Label(login_frame, text="Members Login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=90, y=100)
        
        # Username
        user_label = tk.Label(login_frame, text="Username", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90, y=140)
        self.username = tk.Entry(login_frame, text="Username", font=("Goudy old style", 15), bg="white")
        self.username.place(x=90, y=170, width=320, height=35)
        
        # Password
        password_label = tk.Label(login_frame, text="Password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90, y=210)
        self.password = tk.Entry(login_frame, text="Password", font=("Goudy old style", 15), bg="white")
        self.password.place(x=90, y=240, width=320, height=35)

        # Buttons
        forgot = tk.Button(login_frame, bd=0, text="Forgot Password?", font=("Goudy old style", 15), fg="#6162FF", bg="white").place(x=90, y=280)
        submit = tk.Button(login_frame, command=self.check_login, bd=0, text="Login", font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=90, y=320, width=180, height=40)

    # Check for valid login
    def check_login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error", "All fields required!", parent=self.root)
        elif self.username.get()!="Amen" or self.password.get()!="12345":
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")

def main():
    # Instantiate root Tk window
    root = tk.Tk()

    # Add title to root window
    root.title("Authentication App")

    # Set window dimensions
    root.geometry("1199x688")

    # Make window non-resizable
    root.resizable(False, False)

    # Instantiate login app
    Login(root)

    # Run mainloop
    root.mainloop()

if __name__ == "__main__":
    main()