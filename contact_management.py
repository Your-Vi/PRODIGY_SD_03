import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")

# Edit a contact
def edit_contact():
    contacts = load_contacts()
    view_contacts()
    
    if not contacts:
        return
    
    index = int(input("Enter the contact number to edit: ")) - 1
    if 0 <= index < len(contacts):
        contacts[index]['name'] = input("Enter new Name: ") or contacts[index]['name']
        contacts[index]['phone'] = input("Enter new Phone: ") or contacts[index]['phone']
        contacts[index]['email'] = input("Enter new Email: ") or contacts[index]['email']
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Invalid selection.")

# Delete a contact
def delete_contact():
    contacts = load_contacts()
    view_contacts()
    
    if not contacts:
        return

    index = int(input("Enter the contact number to delete: ")) - 1
    if 0 <= index < len(contacts):
        deleted = contacts.pop(index)
        save_contacts(contacts)
        print(f"Deleted contact: {deleted['name']}")
    else:
        print("Invalid selection.")

# Main menu
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
