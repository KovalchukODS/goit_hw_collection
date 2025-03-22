def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return 'Contact changed'
    except ValueError:
        return 'Contact not found'

def all_contacts(contacts):
    if len(contacts):
        return_str = ''
        for name, phone in contacts.items():
            return_str += f"{name}: {phone}, "
        return return_str[:-2] 
    return 'Contacts not found'

def phone_contact(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return 'Contact not found'
    except IndexError:
        return 'Incorrect input'


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ['exit', 'close']:
            print('Goodbye!')
            break
        elif command == 'hello':
            print(f'''How can I help you?' 
                  There is a list of commands:
                  add
                  change
                  phone
                  all
                  exit''')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(phone_contact(args, contacts))
        elif command == 'all':
            print(all_contacts(contacts))
        else:
            print('Invalid command.')

if __name__ == "__main__":
    main()
