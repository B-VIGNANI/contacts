import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        # Labels and Entries
        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(root, text="Phone Number")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(root, text="Email")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(root, text="Address")
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=4, column=1, padx=10, pady=10)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=5, column=0, padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=5, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and Phone Number are required!")

    def view_contacts(self):
        contacts_str = ""
        for contact in self.contacts:
            contacts_str += f"Name: {contact['name']}, Phone: {contact['phone']}\n"
        messagebox.showinfo("Contact List", contacts_str)

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        found_contacts = [c for c in self.contacts if search_term in c['name'] or search_term in c['phone']]
        contacts_str = ""
        for contact in found_contacts:
            contacts_str += f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}\n"
        if contacts_str:
            messagebox.showinfo("Search Results", contacts_str)
        else:
            messagebox.showinfo("Search Results", "No contacts found.")

    def update_contact(self):
        search_term = simpledialog.askstring("Update Contact", "Enter name or phone number of contact to update:")
        for contact in self.contacts:
            if search_term in contact['name'] or search_term in contact['phone']:
                contact['name'] = simpledialog.askstring("Update Name", "Enter new name:", initialvalue=contact['name'])
                contact['phone'] = simpledialog.askstring("Update Phone", "Enter new phone number:", initialvalue=contact['phone'])
                contact['email'] = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=contact['email'])
                contact['address'] = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contact['address'])
                messagebox.showinfo("Success", "Contact updated successfully!")
                return
        messagebox.showwarning("Update Error", "Contact not found.")

    def delete_contact(self):
        search_term = simpledialog.askstring("Delete Contact", "Enter name or phone number of contact to delete:")
        for contact in self.contacts:
            if search_term in contact['name'] or search_term in contact['phone']:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                return
        messagebox.showwarning("Delete Error", "Contact not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
