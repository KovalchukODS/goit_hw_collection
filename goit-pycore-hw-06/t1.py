from collections import UserDict
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

class Record:
    def __init__(self, contact_name):
        self.name = Name(contact_name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
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
    

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    book = AddressBook()
    
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)
    
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
    
    for name, record in book.data.items():
        print(record)
    
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)
    
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")
    
    book.delete("Jane")