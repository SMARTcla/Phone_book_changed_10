


class Field():
    def __init__(self):
        pass


class Name(Field): 
    
    def __init__(self, forename_):
        self.forename = forename_
        
    def return_name(self):
        return self.forename
        


class Phone(Field):
    def __init__(self, phone_):
        self.phone = list()
        self.phone.append(phone_)
        
    def add_new_number(self, phone_):
        self.phone.append(phone_)
        
        
    def delete_number(self, phone_):
        self.phone.remove(phone_)
        
    def change_number(self, phone_, phone_for_change):
        self.phone[self.phone.index(phone_)] = phone_for_change
        
    def return_phone(self):
        return self.phone
    
class Email(Field):
    def __init__(self, email_):
        self.email = email_

    
    def return_email(self):
        return self.email
    
    
class Record(Name, Phone, Email):
    
    def __init__(self, Name, Phone, Email):
        self.name = Name.forename
        self.email = Email.email
        self.phone = Phone.phone
    
    
        
    
    
    
class AddressBook(Record):
    def __init__(self):
        self.name = list()
        self.phone = list()
        self.email = list()
    
    def add_new_contact(self, contact):
        self.name.append(contact.name)
        self.phone.append(contact.phone)
        self.email.append(contact.email)
    
    def return_names(self):
        return self.name
    
    def return_phones(self):
        return self.phone

    
    
def new_contact():
    print("Enter Name : ")
    name = input()
    _name = Name(name)
    print("Enter Phone : ")
    phone = input()
    _phone = Phone(phone)
    print("Do you want to add email?(y/n)")
    ans = input()
    if ans == 'y':
        print("Enter Email")
        email = input()
    else:
        email = "None"
    _email = Email(email)
    
    
    while(1):
        print("Do you want to add another phone?(y/n)")
        ans = input()
        if ans == 'n':
            break
        if ans == 'y':
            print("Enter Phone : ")
            phone = input()
            _phone.add_new_number(phone)
        else:
            print("You entered uncorrect answer, try again.")
            
    key = Record(_name, _phone, _email)    
    AddressFaceBook.add_new_contact(key)
    
def show_all():
    print("Names")
    print(AddressFaceBook.name)
    print("Phones")
    print(AddressFaceBook.phone)
    print("Emails")
    print(AddressFaceBook.email)  
    
    
def find_contact():
    print("What would you like? Find number by name(1) or name by number(2)?")
    ans = input()
    if ans == "1":
        print("Enter a number")
        ans = input()
        for i in AddressFaceBook.phone:
            for j in i:
                if j == ans:
                    print("The name of this contact :")
                    return AddressFaceBook.name[AddressFaceBook.phone.index(i)]
        print("Phone not found")
    if ans == "2":
        print("Enter a name")
        ans = input()
        try:
            kn = AddressFaceBook.phone[AddressFaceBook.name.index(ans)]
            return kn
        except:
            print("Name not found")
    else:
        return "Wrong choice"
            

def change_num():
    print("Enter a number")
    ans = input()
    answer = "private"
    for i in AddressFaceBook.phone:
        for j in i:
            if j == ans:
                answer = AddressFaceBook.phone.index(i)
    if answer == "private":
        print("Phone not found")
        return 0
    print("Enter a new number")
    ans = input()
    AddressFaceBook.phone[answer] = []
    AddressFaceBook.phone[answer].append(ans)

    
def add_num():
    print("Enter a number")
    ans = input()
    answer = "private"
    for i in AddressFaceBook.phone:
        for j in i:
            if j == ans:
                answer = AddressFaceBook.phone.index(i)
    if answer == "private":
        print("Phone not found")
        return 0
    print("Enter a new number")
    ans = input()
    AddressFaceBook.phone[answer].append(ans)


AddressFaceBook = AddressBook()
print("Hello! My name is Cortana voice assistant!")
print("I was created for control and convenient use of the Address Book.")
print("My functionality is to save the address book, add, delete and change numbers and convenient use of the Address book.")


while(1):
    print("1 - Create new contact")
    print("2 - Search contact")
    print("3 - Change contact")
    print("4 - Show all list")
    print("5 - Add new number")
    print("0 - Exit")
    print("Your choice:")
    choice = input()
    if choice == "1": 
        new_contact()
    elif choice == "2":
        print(find_contact())
    elif choice == "3":
        change_num()
    elif choice == "4": 
        show_all()
    elif choice == "5": 
        add_num()
    elif choice == "0": 
        exit()
    else:
        print("Incorrect choice")
