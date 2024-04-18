"""
Nicola Sciarra
S8125259
- Create a database for the user to 'create' an account
- Define a method to check if username or password is taken
- Create a way to input username and password
- Check if it is correct or incorrect
- If correct access data
NOTE: I mistakenly created a program to create an account and login 
instead of what the assessment task asks for. This is added as extra
stuff for the assessment as it functions really well and I am proud of it.
"""
"""We need to import some libraries"""
import getpass
""" We need a database for creating logins"""
self = None

class Accountdata:
    """
    The self parameter will allow the data inputted to be also specific to the 
    current instance. (In this case I am unsure if it is necessary.)
    """
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

class Database:

    """
    add_user once given that check_user is True and check_pass is True. It will
    assign a new account to the database with the credentials given.
    This is for the create function
    """
    def add_user(self, user, password, firstname, lastname):
        with open("Accountdata.txt", "a") as newuserfile:
            newuserfile.write(f"{lastname} {firstname} {user} {password}\n")
    
    """
    check_user will check each line in the database file in order to check if the 
    given username is already taken. This is for the create function
    """

    def check_user(self, username):
        with open("Accountdata.txt", "r") as database:
            for line in database:
                username == line.strip().split()
                try:
                    if username[2] == username:
                        print("This username is already taken! ")
                        return False
                except IndexError:
                    print("Username must be longer than 2 characters.")
                    return create()
        print("Username is available!")
        return True
    
    """
    check_pass will check each line the database file in order to check if the given
    password is already taken. This is for the create function
    """

    def check_pass(self, password):
        with open("Accountdata.txt", "r") as database:
            for line in database:
                password == line.strip().split()
                try:
                    if password[3] == password:
                        print("This password is already taken! ")
                        return False
                except IndexError:
                    print("Password must be more than 3 characters long!")
                    return create()
        print("Account created successfully! ")
        return True
    
    """
    check_login will check the username and password to see if it lines up with
    any of the accounts given.
    Note: it will only accept if it is correct to the specific line and not the
    entire file as this is how it identifies specific users.
    """

    def check_login(self, username, password):
        db = Database()
        with open("Accountdata.txt", "r") as database:
            for line in database:
                user_data = line.strip().split()
                if user_data[2] == username and user_data[3] == password:
                    return True
        print("The username and/or password are incorrect!")
        return False

    """
    get_name will seek the name of the given username and password so that the
    system knows the users name.
    """

    def get_name(self, username):
        with open("Accountdata.txt", "r") as getname:
            for line in getname:
                getname = line.strip().split()
                if getname[2] == username:
                    return f"{getname[0]} {getname[1]}"


"""We need a main page to select login or create account"""

def main():
    user = input("Would you like to login or create an account? (create/login)")
    if user == 'create':
        return create()
    elif user == 'login':
        return login()
    else:
        print("This is an invalid input.")
        return main()

"""How do we create a login?"""
def create():
    db = Database()
    print("To create an account, please input your information below.")
    firstname = input("What is your firstname? ").capitalize()
    lastname = input("What is your lastname? ").capitalize()
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    if db.check_user(username) and db.check_pass(password):
        db.add_user(username, password, firstname, lastname)
        return login()
    else:
        create()
    
def login():
    db = Database()
    print("To login, please enter the information below")
    username = input("Username: ")
    password = input("Password: ")
    if db.check_login(username, password):
        fullname = db.get_name(username)
        if fullname:
            print(f"Welcome {fullname} to Nicola's Assessment task!")
            return home()
        else:
            print("Welcome to Nicola's Assessment task!\n"
                  "It seems that there is no name assigned to this user\n"
                  "Please contact assistance if needed.")
            return home()
    else:
        login()
    
def home():
    choice = input("What would you like to do?\n"
                   "1. Open Accountdata.txt information\n"
                   "2. Logout")
    if choice == '1':
        print_file()

def print_file():
    try:
        with open("Accountdata.txt" "r") as readfile:
            readfile.readlines
            print(readfile)
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()