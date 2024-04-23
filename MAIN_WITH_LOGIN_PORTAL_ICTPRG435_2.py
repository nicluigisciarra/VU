"""
This is the main assessment of ICTPRG435 Task 2 COMBINED with the attached login portal
Student Name: Nicola Sciarra
Student Number: s8125259
Assignment: ICTPRG435 Task2

Initially I mistakenly believed we needed to create a login page.
Once I managed to complete it (4 hours later) I quickly realised that 
it is a password manager which is needed for the assessment.
I then had an idea click which I believed I can combine the 2 programs.
I quickly got started and with the knowledge I had it was much quicker for me to 
accomplish. I finished the main task then decided I will move the code of both files
into a new python program which will act as a LOGIN PORTAL, then once logged in,
access the ACCOUNT INFORMATION. My goal with this is to ensure that when you
create an account in the LOGIN PORTAL, it will create a new text file named after
that account which logged in and will consist of their own account information
for the websites they wish to input. Through this, different users can access their
own account information but not other account information. To add more security I
could add encryption to the login portal and account information saved in each text file,
but that can be a fun task for me in the future as I am extremely pleased with the work
I accomplished.
"""
import time
import getpass
import sys, os
website = None
username = None
password = None

class Accountdata:
    """
    The self parameter will allow the data inputted to be also specific to the 
    current instance. (In this case I am unsure if it is necessary. I saw people
    use it a lot)
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
        try:
            with open("Accountdata.txt", "r") as database:
                for line in database:
                    user = line.strip().split()[2]
                    try:
                        if user == username:
                            print("This username is already taken! ")
                            return False
                    except IndexError:
                        print("Invalid username!")
                        return create()
            print("Username is available!")
            return True
        except FileNotFoundError:
            with open("Accountdata.txt", "w") as newdatabase:
                return True
    """
    check_pass will check each line the database file in order to check if the given
    password is already taken. This is for the create function
    """

    def check_pass(self, password):
        with open("Accountdata.txt", "r") as database:
            for line in database:
                passw = line.strip().split()[3]
                try:
                    if passw == password:
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
                    return f"{getname[1]} {getname[0]}"

    """
    get_username will seek the username of the current user.
    """
    
    def get_username(self, username):
        with open("Accountdata.txt", "r") as getusername:
            for line in getusername:
                getusername = line.strip().split()
                if getusername[2] == username:
                    return f"{username}"

"""
The main interactive portal which you can choose to create or login.
"""           
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

"""
How will we login to the account we created?
"""
def login():
    db = Database()
    print("To login, please enter the information below")
    username = input("Username: ")
    password = input("Password: ")
    if db.check_login(username, password):
        fullname = db.get_name(username)
        print("Logging in...")
        time.sleep(1)
        clear()
        if fullname:
            print(f"Welcome {fullname} to Nicola's Assessment task!")
            return home(username)
        else:
            print("Welcome to Nicola's Assessment task!\n"
                "It seems that there is no name assigned to this user\n"
                "Please contact assistance if needed.")
            return home(username)
    else:
        login()
    
"""
The home page of the LOGIN PORTAL, this is where we are logged in to the account
and can access the password manager
"""

def home(username):
        choice = input("What would you like to do?\n"
                    "1. Enter Password Manager\n"
                    "2. Logout\n")
        if choice == '1':
            return main0(username)
        elif choice == '2':
            return login()
        else:
            invalid()

"""
here we will create a class for UserData this will function as a way to:
- add account information
- search for account information
- check if the account is already added to the system to avoid overflow
- an enquiry to add another
- reveal the web list
as you can see in this class, we transferred the username value from the LOGIN PORTAL
to ensure that all data that will be created is only associated with the username.
in open(f"{username}data.txt) it will write if its a new account, but also append
or read when necessary in the code (when it is called).
"""

class UserData:
    def add_acc_inf(self, website, username, accountname, accountpassword):
        try:
            with open(f"{username}data.txt", "a") as newacc:
                newacc.write(f"{website} {accountname} {accountpassword}\n")
                print(f"Account for {website} saved!")
                time.sleep(1)
            open(f"{username}data.txt", "r")
            print("Your list of accounts has successfully updated! ")
            return main0(username)
        except FileNotFoundError:
            with open(f"{username}data.txt", "w") as newacc:
                newacc.write(f"{website} {accountname} {accountpassword}")
                print(f"Account for {website} saved!")
                return main0(username)

    def search_acc_inf(self, username, website):
        found = False
        ud = UserData()
        try:
            print(f"Searching for account in {username}...")
            time.sleep(1)
            with open(f"{username}data.txt", "r") as readacc:
                for line in readacc:
                    linedata = line.strip().split()
                    if website == linedata[0]:
                        accountname = linedata[1]
                        accountpassword = linedata[2]
                        print(f"Here is the account data for {website}\n"
                              f"Username: {accountname}\n"
                              f"Password: {accountpassword}")
                        found = True
                        return ud.search_acc_enq(username)
    
        except FileNotFoundError:
            newuser = input("There was no data stored in this system.\n"
                   "Would you like to add a new account? (yes/no)\n").lower()
            if newuser in ['yes', 'y']:
                return new_accinf(username)
            elif newuser in ['no', 'n']:
                return main0(username)
        if not found:
            user = input("There was no data found in the system, \n"
            + "Would you like to search again? (yes/no) \n").lower()
            if user in ['yes', 'y']:
                return search_acc(username)
            elif user in ['n', 'no']:
                return main0(username)
            else:
                invalid()
                return search_acc(username)
            
        

            
            
    def check_webdata(self, website, username, accountname, accountpassword):
        try:
            with open(f"{username}data.txt", "r") as checkinf:
                for line in checkinf:
                    webdata = line.strip().split()
                    if website == webdata[0] and accountname == webdata[1] and accountpassword == webdata[2]:
                        print("Account already added!")
                        return main0(username)
                    else:
                        return print("Adding new account")
                        
        except FileNotFoundError:
            print("No accounts saved")
            pass                     
        
    def search_acc_enq(self, username):
        user = input("Would you like to search for anything else? (yes/no)\n")
        if user.lower() in ['yes', 'y']:
            return search_acc(username)
        elif user.lower() in ['n', 'no']:
            return main0(username)
        else:
            invalid()
            return UserData.search_acc_enq(username)
        
    
    def show_weblist(self, username):
        ud = UserData()
        try:
            with open(f"{username}data.txt", "r") as webdata:
                for line in webdata:
                    website = line.strip().split()[0]
                    if not website:
                        print("There is no websites with account data.")
                        user = input("Would you like to add one?").lower()
                        if user in ['yes', 'y']:
                            return new_accinf(username)
                        elif user in ['no', 'n']:
                            return main0(username)
                        else:
                            return main0(username)
                    else:
                        print(website)
                        
            website = input("Which website would you like to search?\n").capitalize()
            if not website:
                print(f"There is no account data for {website}\n"
                      "Please check if it was spelt correctly!")
                return main0(username)
            webdata.close
            return ud.search_acc_inf(username, website)

        except FileNotFoundError:
            print("There is no information saved.")
            nouser = input("Would you like to add an account? (yes/no)").lower
            if nouser in ['y', 'yes']:
                return new_accinf(username)
            elif nouser in ['n', 'no']:
                return main0(username)
            else:
                invalid()
                return main0(username)
    

"""
in new_accinf, it will give us the values required to save it in the personal
text file.
"""       

def new_accinf(username):
    ud = UserData()
    website = input("What is the website for the account? \n").capitalize()
    accountname = input(f"What is the username/email for {website}? \n")
    accountpassword = input(f"What is the password for {website}? \n")
    ud.check_webdata(website, username, accountname, accountpassword)
    ud.add_acc_inf(website, username, accountname, accountpassword)

"""
search_acc will search for a specific website and give the account information.
"""

def search_acc(username):
    ud = UserData()
    website = input("Website Search (Website name): ").capitalize()
    return ud.search_acc_inf(website, username)

"""
I quickly realised for every function, there will most likely be an invalid input
so i then created a function called invalid to quickly respond to an invalid input
"""

def invalid():
    print("Invalid input")

"""
Here we have is the main page of the password manager to allow users to select what
they would like to do in the password manager
"""

def main0(username):
    print(f"Accessing account database for {username}...")
    db = Database()
    ud = UserData()
    fullname = db.get_name(username)
    time.sleep(1)
    clear()
    try:
        
        with open(f"{username}data.txt", "r") as readfile:
            userstart = input(f"Hello {fullname}! Welcome to your personal password manager!\n"
                        "What would you like to do?\n"
                        "1. Add new account information\n"
                        "2. Search for account\n"
                        "3. Show websites that have saved account info\n"
                        "4. Logout\n"
                        "5. Exit Password Manager\n")

            if userstart == '1':
                return new_accinf(username)
            elif userstart == '2':
                return search_acc(username)
            elif userstart == '3':
                ud.show_weblist(username)
            elif userstart == '4':
                main()
            elif userstart == '5':
                exit()
            else:
                print("Invalid input, please type one of the numbers as your choice.\n")
                return main0(username)
    except FileNotFoundError:
        print("It looks like you have not yet added information!")
        userfresh = input("Would you like to add a new account? (yes/no)").lower()
        if userfresh in ['yes', 'y']:
            new_accinf(username)

def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

"""
calls the main function to start the program.
"""
    
if __name__ == '__main__':
    main()


#DEBUG NOTES:
# - When searching for a website, it will always say no data found. DONE
# - Everytime you consistently add new account, it will overlap and rewrite  
#   new account added for every time the function is run. DONE
# - When no data stored then asks would you like to add new account?
# - When no, still prompts for website of account.
# - When it says username already taken maybe ask if you would like to login
# - Add option to delete already made accounts
# - It is way too easy to accidentally create an account.
# - when repeatedly searching it eventually says no account found even when there is