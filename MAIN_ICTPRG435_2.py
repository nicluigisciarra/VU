"""This is the main assessment of ICTPRG435 Task 2."""
import time
from colorama import Fore, Back, init, Style
website = None
username = None
password = None
start = True
    
class UserData:
    def add_acc_inf(website, username, password):
        try:
            with open("webaccountdata.txt", "a") as newacc:
                newacc.write(f"{website} {username} {password}\n")
                print(f"Account for {website} saved!")
                time.sleep(1)
            open("webaccountdata.txt", "r")
            print("Your list of accounts has successfully updated! ")
            return main0()
        except FileNotFoundError:
            with open("webaccountdata.txt", "w") as newacc:
                newacc.write(f"{website} {username} {password}")
                print(f"Account for {website} saved!")
                return main0()

    def search_acc_inf(website):
        found = False
        try:
            print("Searching...")
            time.sleep(1)
            with open("webaccountdata.txt", "r") as readacc:
                for line in readacc:
                    linedata = line.strip().split()
                    if website == linedata[0]:
                        username = linedata[1]
                        password = linedata[2]
                        print(f"Here is the account data for {website}\n"
                              f"Username: {username}\n"
                              f"Password: {password}")
                        found = True
                        return UserData.search_acc_enq()
        except FileNotFoundError:
            newuser = input(Fore.RED + "There was no data stored in this system.\n" + Fore.GREEN
                  + "Would you like to add a new account? (yes/no)\n")
            if newuser == 'yes' or 'y' or 'Yes':
                return new_accinf()
        if not found:
            user = input(Fore.RED + "There was no data found in the system, \n" + Fore.GREEN
                        + "would you like to search again? \n")
            if user.lower() in ['yes', 'y']:
                return search_acc()
            elif user.lower() in ['n', 'no']:
                return main0()
            else:
                invalid()
                return search_acc()
        

            
            
    def check_webdata(website, username, password):
        with open("webaccountdata.txt", "r") as checkinf:
            for line in checkinf:
                webdata = line.strip().split()
                if website == webdata[0] and username == webdata[1] and password == webdata[2]:
                    print("Account already added!")
                    return new_accinf()
                else:
                    continue                       
        
    def search_acc_enq():
        user = input("Would you like to search for anything else? (yes/no)\n")
        if user.lower() in ['yes', 'y']:
            return search_acc()
        elif user.lower() in ['n', 'no']:
            return main0()
        else:
            invalid()
            return UserData.search_acc_enq()
        
    
    def show_weblist():
        try:
            with open("webaccountdata.txt", "r") as webdata:
                for line in webdata:
                    website = line.strip().split()[0]
                    if not website:
                        print("There is no websites with account data.")
                        user = input("Would you like to add one?").lower()
                        if user in ['yes', 'y']:
                            return new_accinf()
                        else:
                            return main0()
                    else:
                        print(website)
                        
            user = input("Which website would you like to search?\n").capitalize()
            return UserData.search_acc_inf(user)

        except FileNotFoundError:
            print("There is no information saved.")
            nouser = input("Would you like to add an account? (yes/no)").lower
            if nouser in ['y', 'yes']:
                return new_accinf()
            if nouser in ['n', 'no']:
                return main0()
            else:
                invalid()
                return main0()
    

def new_accinf():
    website = input("What is the website for the account? \n").capitalize()
    username = input(f"What is the username/email for {website}? \n")
    password = input(f"What is the password for {website}? \n")
    UserData.check_webdata(website, username, password)
    UserData.add_acc_inf(website, username, password)

def search_acc():
    website = input("Website Search (Website name): ").capitalize()
    return UserData.search_acc_inf(website)


def invalid():
    print(Fore.RED + "Invalid input" + Fore.GREEN)

def main0():
    print(Fore.GREEN)
    print(Back.BLACK)
    userstart = input(f"Hello! Welcome to your personal password manager!\n"
                "What would you like to do?\n"
                "1. Add new account information\n"
                "2. Search for account\n"
                "3. Show websites that have saved account info\n"
                "4. Exit\n")
    if userstart == '1':
        return new_accinf()
    elif userstart == '2':
        return search_acc()
    elif userstart == '3':
        UserData.show_weblist()
    elif userstart == '4':
        print(Fore.RESET)
        exit()
    else:
        print(Fore.RED + "Invalid input, please type one of the numbers as your choice.\n"
            + Fore.GREEN)
        return main0()
    
if __name__ == '__main__':
    main0()