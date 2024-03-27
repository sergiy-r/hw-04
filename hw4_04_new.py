# Module 4 Homework: Exercise 4
# This is program for a Command Line Interface bot that allows to interact with a contact list
# It allows a user to add, change, and retrieve a contact's phone number, as well as print all contacts
# Names and commands are case-insensitive.

# parses user input
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# adds name and phone to a dictionary 'contacts'
def add_contact(args, contacts):
    name, phone = args
    contacts[name.title()] = phone
    return "Contact added."


# changes a phone number for a name in contacts dictionary
def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts.update({name: phone})
        return "Contact updated."
    else:
        return "No matching contact found. No updates made."


# returns the phone number for a name from contacts dictionary
def phone(name, contacts):
    if contacts.get(name):
        return contacts.get(name)
    else:
        return "No matching contact found."


# returns all names and numbers from contacts dictionary
def show_all(contacts):
    if contacts:
        contacts_str ="\n".join(f"{name}: {phone}" for name, phone in contacts.items())
        return "Contacts:\n" + contacts_str
    else:
        return "No contacts have been added yet."


# main function for processing user input, output and logic of the CLI bot
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi"]:
            print("How can I help you?")
        elif command == "add":
            try:
                if args[0].title() in (key for key in contacts):
                    print("This contact already exists. The contact hasn't been added.")
                else:
                    args = [args[0].title(), args[1]]
                    print(add_contact(args, contacts))
            except Exception:
                print("The details entered are incorrect. Enter 'add' [Name] [Number], e.g., add Bob 07771110011")
        elif command in ["change", "update"]:
            try:
                args = [args[0].title(), args[1]]
                print(change_contact(args, contacts))
            except Exception:
                print("The details entered are incorrect. Enter 'change' [Name] [Number], e.g., change Bob 07771110011")
        elif command == "phone":
            print(phone(args[0].title(), contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()



