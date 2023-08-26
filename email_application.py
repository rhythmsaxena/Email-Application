import tkinter as tk
from tkinter import messagebox


class EmailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Application")
        self.root.geometry("300x250")

        self.logged_in = False
        self.current_user = None

        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)
        self.password_label = tk.Label(root, text="Password:")
        self.password_entry = tk.Entry(root, show="*")
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.logout_button = tk.Button(root, text="Logout", command=self.logout)
        self.to_label = tk.Label(root, text="To:")
        self.to_entry = tk.Entry(root)
        self.subject_label = tk.Label(root, text="Subject:")
        self.subject_entry = tk.Entry(root)
        self.message_label = tk.Label(root, text="Message:")
        self.message_text = tk.Text(root, height=5, width=30)
        self.send_button = tk.Button(root, text="Send Email", command=self.send_email)

        self.email_label.pack()
        self.email_entry.pack(fill="x")
        self.password_label.pack()
        self.password_entry.pack(fill="x")
        self.login_button.pack()
        self.logout_button.pack()
        self.to_label.pack()
        self.to_entry.pack(fill="x")
        self.subject_label.pack()
        self.subject_entry.pack(fill="x")
        self.message_label.pack()
        self.message_text.pack(fill="both")
        self.send_button.pack()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Add your own authentication logic here

        if email == "test@example.com" and password == "password":
            self.logged_in = True
            self.current_user = email
            messagebox.showinfo("Login", "Logged in successfully.")
        else:
            messagebox.showerror("Login", "Invalid credentials.")

    def logout(self):
        self.logged_in = False
        self.current_user = None
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        messagebox.showinfo("Logout", "Logged out successfully.")

    def send_email(self):
        if not self.logged_in:
            messagebox.showerror("Error", "Please log in first.")
            return

        # Add your email sending logic here

        to_email = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", "end-1c")

        messagebox.showinfo("Email Sent",
                            f"Email sent from {self.current_user} to {to_email}.\n\nSubject: {subject}\nMessage:\n{message}")


if __name__ == "__main__":
    root = tk.Tk()
    email_app = EmailApp(root)
    root.mainloop()
