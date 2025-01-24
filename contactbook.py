class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        print("\n--- Add New Contact ---")
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        print("\n--- Contact List ---")
        if not self.contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self):
        print("\n--- Search Contact ---")
        search_term = input("Enter name or phone number to search: ").lower()
        found_contacts = [
            contact for contact in self.contacts
            if search_term in contact.name.lower() or search_term in contact.phone
        ]
        if found_contacts:
            print("\nSearch Results:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No matching contacts found.")

    def update_contact(self):
        self.view_contacts()
        if not self.contacts:
            return
        try:
            contact_index = int(input("Enter the number of the contact to update: ")) - 1
            if 0 <= contact_index < len(self.contacts):
                contact = self.contacts[contact_index]
                print(f"\nUpdating contact: {contact}")
                contact.name = input(f"Enter new name ({contact.name}): ") or contact.name
                contact.phone = input(f"Enter new phone number ({contact.phone}): ") or contact.phone
                contact.email = input(f"Enter new email ({contact.email}): ") or contact.email
                contact.address = input(f"Enter new address ({contact.address}): ") or contact.address
                print("Contact updated successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def delete_contact(self):
        self.view_contacts()
        if not self.contacts:
            return
        try:
            contact_index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= contact_index < len(self.contacts):
                deleted_contact = self.contacts.pop(contact_index)
                print(f"Contact '{deleted_contact.name}' deleted successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    contact_book = ContactBook()
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()