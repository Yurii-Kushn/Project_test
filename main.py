from datetime import date, datetime
import re
from addres_book import *
from Notebook import *


class Name:
    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value


class Phone:
    def __init__(self):
        while True:
            self.values = []
            self.value = input("Enter phones with code: +38 plus 10 numbers after:")
            try:
                for number in self.value.split(' '):
                    if re.match('^\\+38\d{10}$', number):
                        self.values.append(number)
                    else:
                        raise ValueError
            except ValueError:
                print('Incorrect phone number!')
            else:
                break

    def __getitem__(self):
        return self.values


class Address:
    def __init__(self, value=""):
        self.value = value

    def __getitem__(self):
        return self.value


class Birthday:
    def __init__(self, value=''):
        while True:
            if value:
                self.value = value
            else:
                self.value = input("Birthday date in format: day/month/year: ")
            try:
                if re.match('^\d{2}/\d{2}/\d{2}$', self.value):
                    self.value = datetime.strptime(self.value, "%d/%m/%y")
                    break
                elif self.value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect date! Please provide correct date format.')

    def __getitem__(self):
        return self.value


class Email:

    def __init__(self, value=''):
        while True:
            if value:
                self.value = value
            else:
                self.value = input("Email: ")
            try:
                if re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.value):
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect email! Please enter right email.')

    def __getitem__(self):
        return self.value


class Record:
    def __init__(self, name="", phones='', address='', birthday='', email=''):
        self.name = name
        self.phones = phones
        self.address = address
        self.birthday = birthday
        self.email = email

    def __str__(self):
        return (f"Contact name: {self.name},\nphones: {self.phones},\n"
                f"email: {self.email},\nbirthday: {self.birthday},\naddress: {self.address}")


class Bot:
    def __init__(self):
        self.book = AddressBook()

    def handle(self, action):
        if action == 'add':
            name = Name(input("Name: ")).value.strip()
            phones = Phone().value
            birthday = Birthday().value
            email = Email().value.strip()
            address = Address(input("Address: ")).value.strip()
            record = Record(name, phones, address, birthday, email)
            print(record)
            return self.book.add(record)
        elif action == 'search':
            pattern = input('Enter Search pattern: ')
            result = self.book.search_by_match(pattern)
            for account in result:
                print(account)
        elif action == 'edit':
            contact_name = input('Contact name: ')
            parameter = input('Which parameter to edit(phones, birthday, address, email): ').strip()
            #new_value = input("New Value: ")
            return self.book.editing_contact(contact_name, parameter)
        elif action == 'remove':
            contact_name = input('Contact name: ')
            return self.book.delete(contact_name)
        elif action == 'save':
            file_name = input("File name: ")
            return self.book.save(file_name)
        elif action == 'load':
            file_name = input("File name: ")
            return self.book.load(file_name)
        elif action == 'congratulate':
            days = input("Enter the number of days until Birthday: ")
            print(self.book.list_contacts_with_day_of_birthday(days))
        elif action == 'view':
            print(self.book)
        elif action == 'exit':
            pass
        else:
            print("There is no such command!")


def main():
    command = ""
    bot = Bot()
    bot.book.load("auto_save")
    commands_help = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        command = input("Enter your command or the command Help to see a list of commands: ").lower()
        if command == 'help':
            format_str = str('{:%s%d}' % ('^', 20))
            for command in commands_help:
                print(format_str.format(command))
            command = input().strip().lower()
            bot.handle(command)
            if command in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        else:
            bot.handle(command)
            if command in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if command == 'exit':
            print("Good bay")
            break


if __name__ == '__main__':
    main()

# book = AddressBook()
#
# john_record = Record("John", "21/11/95")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# book.add_record(john_record)
#
# jane_record = Record("Jane", "11/3/96")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)
#
# misha_record = Record("Misha", "24/8/94")
# misha_record.add_phone("9876543210")
# book.add_record(misha_record)
#
# for i in book.iterator():
#     print(i)
#
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")
#
# print(john)
#
# found_phone = john.find_phone("5555555555")
# print(f"{john.name.value}: {found_phone.value}")
#
# book.delete("Jane")
#
# for i in book.iterator():
#     print(i)
#
# searching = book.search_by_match("765")
# print(searching)
#
# with open("address_book.bin", "wb") as file:
#     pickle.dump(book, file)
#
# with open("address_book.bin", "rb") as file:
#     content = pickle.load(file)
#     print(f"loading_address_book:{content}")
