contacts = []

with open("contacts.txt", "r") as file:
    for line in file:
        name, number, email = line.strip().split(" | ")
        contact = {
            "name": name,
            "number": number,
            "email": email
        }
        contacts.append(contact)

while True:
    print("Welcome to the Contact List App!")
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Search contacts")
    print("4. Delete a contact")
    print("5. Exit")

    answer = float(input("Enter your choice: "))
    if answer == 1:
        while True:
            add = input("would you like to add a contact? ")
            if add.lower() == "yes":
                name = input("what is the contact's name? ")
                try:
                    number = int(input("what is the contact's number? "))
                except ValueError:
                    print("Invalid input. Please enter a valid phone number.")
                    continue

                email = input("what is the contact's email? ")

                contact = {
                "name": name,
                "number": number,
                "email": email
                }

                contacts.append(contact)

            elif add.lower() == "no":
                break

            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    if answer == 2:
        print("Contacts List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Number: {contact['number']}, Email: {contact['email']}")

    if answer == 3:
        search_name = input("Enter the name of the contact you want to search for: ")
        found_search = False
        
        for contact in contacts:
            if search_name.lower() == contact["name"] :
                found_search = True
                print ("contact found")
                print(f"Name: {contact['name']}, Number: {contact['number']}, Email: {contact['email']}")
        if not found_search:
                print("Contact not found.Please check the name and try again.")

    if answer == 4:
        delete = input("Enter the name of the contact you want to delete: ")

        found = False
        new_contacts = []

        for contact in contacts:
            if delete.lower() == contact["name"].lower():
                found = True
            else:
                new_contacts.append(contact)

        if found:
            print(f"Contact {delete} deleted successfully.")
        else:
            print("Contact not found. Please check the name and try again.")

        contacts = new_contacts
    if answer == 5:
        break

with open("contacts.txt", "w") as file:
    for contact in contacts:
        file.write(f"{contact['name']} | {contact['number']} | {contact['email']}\n")