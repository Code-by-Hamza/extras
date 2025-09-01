import json

filename = "contacts.json"

#load
def load_contacts():
    try:
        with open(filename,"r") as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return []

#save
def save_contacts(contacts):
    with open(filename,"w") as f:
        json.dump(contacts,f,indent=4)

#menu
def menu():
    print("\n---CONTACTS---")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5.Save & Exit")

#view 
def view(contacts):
    if not contacts:
        print("Not Found")
        return
    for i,contact in enumerate(contacts,start=1):
        print(f"{i}. Name:{contact['name']}, Phone:{contact['phone']}")

#add 
def add(contacts):
    name = input("Enter Name:")
    phone = input("Enter Phone No.:")

    contact = {
        "name" : name,
        "phone": phone
    }
    
    contacts.append(contact)
    print(f"Contact: '{name}' Saved Successfully")

#search for a contact 
def search(contacts):
    searched = input("Enter a Name:")
    found = False
    for contact in contacts:
        if contact["name"].lower() == searched.lower():
            print(f"Found! \n Name: {contact['name']}, Phone: {contact['phone']}")
            found = True
            break
    if not found:
        print("Not Found!")

#delete
def delete(contacts):
    name = input("Enter a Name to Delete:")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact: '{name}' Removed!")
            found = True
            break
    if not found:
        print("Name does not Exist!")

#main loop
def main():
    contacts = load_contacts()

    while True:
        menu()
        cho = input("\nEnter a Number: ")
        if cho == "1":
            view(contacts)
        elif cho == "2":
            add(contacts)
        elif cho == "3":
            search(contacts)
        elif cho == "4":
            delete(contacts)
        elif cho == "5":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()


