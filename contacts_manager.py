
import json
import csv
import re
from pathlib import Path

DATA_FILE = Path("contacts_data.json")


def load_contacts():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_contacts(contacts):
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()
    if not re.fullmatch(r"\+?\d{10,15}", phone):
        print("Invalid phone number.")
        return

    email = input("Enter email: ").strip()
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        print("Invalid email.")
        return

    contacts[name.lower()] = {
        "name": name,
        "phone": phone,
        "email": email
    }
    save_contacts(contacts)
    print("Contact added successfully!")


def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for contact in contacts.values():
        print(
            f"Name: {contact['name']} | "
            f"Phone: {contact['phone']} | "
            f"Email: {contact['email']}"
        )


def search_contact(contacts):
    name = input("Enter name to search: ").strip().lower()
    contact = contacts.get(name)

    if contact:
        print(contact)
    else:
        print("Contact not found.")


def update_contact(contacts):
    name = input("Enter the name to update: ").strip().lower()

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter new phone number: ").strip()
    if not re.fullmatch(r"\+?\d{10,15}", phone):
        print("Invalid phone number.")
        return

    email = input("Enter new email: ").strip()
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        print("Invalid email.")
        return

    contacts[name]["phone"] = phone
    contacts[name]["email"] = email
    save_contacts(contacts)
    print("Contact updated successfully!")


def delete_contact(contacts):
    name = input("Enter the name to delete: ").strip().lower()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def export_contacts(contacts):
    with open("contacts_export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])

        for contact in contacts.values():
            writer.writerow([
                contact["name"],
                contact["phone"],
                contact["email"]
            ])

    print("Contacts exported to contacts_export.csv")


def main():
    contacts = load_contacts()

    while True:
        print("\n--- CONTACT MANAGEMENT SYSTEM ---")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export Contacts to CSV")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            display_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            export_contacts(contacts)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
  
