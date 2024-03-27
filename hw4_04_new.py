# Module 4 Homework: Exercise 4
# This is program for a Command Line Interface bot that allows to interact with a contact list
# It allows a user to add, change, and retrieve a contact's phone number, as well as print all contacts
# Names are case-insensitive.
# For a list of commands enter 'help'

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name.title()] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    for saved_name in contacts:
        if saved_name.casefold() == name.casefold():
            contacts[saved_name] = phone
            return "Contact updated."
        else:
            return "No matching contact found. No updates made."


def phone(name, contacts):
    if contacts.get(name):
        return contacts.get(name)
    else:
        return "No matching contact found."

def show_all(contacts):
    if contacts:
        return contacts
    else:
        return "No contacts have been added yet."


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
                print("Args: ", args)
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



