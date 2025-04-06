from collections import UserDict
from datetime import datetime as dtdt, timedelta as td
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, contact_name):
         if not contact_name:
            raise ValueError("Name is required!")
         super().__init__(contact_name)

class Phone(Field):
    def __init__(self, value):
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Phone number must be exactly 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.date = dtdt.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)

class Record:
    def __init__(self, contact_name):
        self.name = Name(contact_name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones)
        birthday_str = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"
    
    def add_phone(self, contact_phone):
        self.phones.append(Phone(contact_phone))
    
    def remove_phone(self, contact_phone):
        self.phones = [p for p in self.phones if p.value != contact_phone]
    
    def edit_phone(self, old_phone_num, new_phone_num):
        for p in self.phones:
            if p.value == old_phone_num:
                p.value = new_phone_num
                return
        raise ValueError("Old phone number not found.")
    
    def find_phone(self, phone):
        return next((p.value for p in self.phones if p.value == phone), None)
    
    def add_birthday(self, birthdate):
            self.add_birthday = Birthday(birthdate)

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        current_day = dtdt.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday = dtdt.strptime(record.birthday.value, "%d.%m.%Y").date()
                birthday_this_year = birthday.replace(year=current_day.year)

                if birthday_this_year < current_day:
                    birthday_this_year = birthday_this_year.replace(year=current_day.year + 1)

                days_until_birthday = (birthday_this_year - current_day).days

                if 0 <= days_until_birthday <= 7:
                    congratulation_date = birthday_this_year
                    if congratulation_date.weekday() in [5, 6]:  # Saturday, Sunday
                        congratulation_date += td(days=(7 - congratulation_date.weekday()))

                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                    })

        return upcoming_birthdays

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError) as e:
            return str(e)
    return wrapper

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError) as e:
            return str(e)
    return wrapper

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.edit_phone(old_phone, new_phone)
    return "Phone number updated."

@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    return f"{name}'s phones: {', '.join(p.value for p in record.phones)}"

def show_all(book: AddressBook):
    if not book.data:
        return "Address book is empty."
    return '\n'.join(str(record) for record in book.values())

@input_error
def add_birthday(args, book: AddressBook):
    name, birthdate = args
    record = book.find(name)
    if not record:
        return "Contact not found."
    record.add_birthday(birthdate)
    return "Birthday added."

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found."
    if not record.birthday:
        return "Birthday not set."
    return f"{name}'s birthday: {record.birthday.value}"

@input_error
def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays this week."
    return '\n'.join(f"{u['name']}: {u['congratulation_date']}" for u in upcoming)


def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

if __name__ == "__main__":
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print("Invalid command.")