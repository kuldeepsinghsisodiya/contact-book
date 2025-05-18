import tkinter as tk
from tkinter import messagebox

# Contact dictionary to store contacts
contacts = {}

# Function to add contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if name and phone:
        contacts[name] = {'Phone': phone, 'Email': email}
        messagebox.showinfo("Success", f"Contact '{name}' added!")
        clear_entries()
        show_contacts()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required!")

# Function to delete contact
def delete_contact():
    name = entry_name.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
        clear_entries()
        show_contacts()
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

# Function to search contact
def search_contact():
    name = entry_name.get()
    if name in contacts:
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_phone.insert(0, contacts[name]['Phone'])
        entry_email.insert(0, contacts[name]['Email'])
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

# Function to clear input fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Function to display all contacts
def show_contacts():
    text_area.delete('1.0', tk.END)
    for name, details in contacts.items():
        contact_info = f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}\n"
        text_area.insert(tk.END, contact_info)

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x450")

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)
tk.Button(root, text="Show All Contacts", command=show_contacts).pack(pady=5)

text_area = tk.Text(root, height=10, width=50)
text_area.pack(pady=10)

root.mainloop()

