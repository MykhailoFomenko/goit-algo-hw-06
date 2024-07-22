from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
		pass


class Phone(Field):
	def __init__(self, value):
            super().__init__(value)
            if 10 != len(value) or not value.isdigit():
                raise ValueError("Phone has incorrect format")
      

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
            phone_object = Phone(phone)
            self.phones.append(phone_object.value)

    def remove_phone(self, phone):
         self.phones.remove(phone)
        
    def edit_phone(self, old_number, new_number):
          if old_number not in self.phones or len(new_number) != 10 or not old_number.isdigit() or not new_number.isdigit():
            raise ValueError("One of phones or both of them have incorrect format")
          else:
            self.phones[self.phones.index(old_number)] = new_number

    def find_phone(self, phone):
        if phone in self.phones:
            return Phone(phone)
        else:
             return None
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, contact): 
        self.data.update({contact.name.value : contact.phones})     

    def find(self, name):
        if name in self.data:
           contact = Record(name)
           for el in self.data.get(name):
                 contact.add_phone(el)
           self.data.update({contact.name.value : contact.phones})  
           return contact
        else:
            return None
        
    def delete(self, name):
          self.data.pop(name)

    def __str__(self):
        return f"Book of contacts: {self.data}"


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі     
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")