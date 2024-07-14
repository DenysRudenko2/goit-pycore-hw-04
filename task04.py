import json
import sys


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_username_phone(args, contacts):
    name, phone = args
    contacts[name] = phone

    return "Contact added."


def change_username_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def phone_username(args, contacts):
    [name] = args
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def all_contacts(contacts):
    return json.dumps(contacts, sort_keys=True, indent=4)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    try:
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_username_phone(args, contacts))
            elif command == "change":
                print(change_username_phone(args, contacts))
            elif command == "phone":
                print(phone_username(args, contacts))
            elif command == "all":
                print(all_contacts(contacts))

            else:
                print("Invalid command.")
    except ValueError as error:
        sys.stderr.write(f'Invalid command.: {str(error)}\n')


if __name__ == "__main__":
    main()
