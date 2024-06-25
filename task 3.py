import json
import os

# Define the Contact class
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

    @staticmethod
    def from_dict(data):
        return Contact(data['name'], data['phone'], data['email'])

# File to store the contacts
CONTACTS_FILE = 'contacts.json'

# Load contacts from the file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            contacts_data = json.load(file)
            return [Contact.from_dict(contact) for contact in contacts_data]
    return []

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump([contact.to_dict() for contact in contacts], file)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    contacts.append(Contact(name, phone, email))
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts):
            print(f"{idx + 1}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

# Edit an existing contact
def edit_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the contact number you want to edit: ")) - 1
    if 0 <= index < len(contacts):
        contacts[index].name = input(f"Enter new name (current: {contacts[index].name}): ")
        contacts[index].phone = input(f"Enter new phone (current: {contacts[index].phone}): ")
        contacts[index].email = input(f"Enter new email (current: {contacts[index].email}): ")
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the contact number you want to delete: ")) - 1
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

# Main program loop
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

