from Util import db_helper as db
from Util import session_info as account
import MainMenu as Menu
import re


class Login:
    def menu(self):
        print("##################################################")
        print("# \"When I had just graduated, I had a hard time  #")
        print("# trying to get companies to accept me withe no  #")
        print("# experience, but thanks to InCollege, I learned #")
        print("# skills that employers wanted, and was able to  #")
        print("# connect with them. I recommend InCollge to all #")
        print("# students in college that want to get hired as  #")
        print("# soon as they graduate.\"                        #")
        print("##################################################")
        print("Welcome to InCollege: ")
        print("1.) Sign In")
        print("2.) Create Account")
        print("3.) Search for someone you know")
        print("4.) Why should you join InCollege?")
        print("5.) Exit")
        option = int(input("Enter Option: "))
        if option == 1:
            self.sign_in()
        elif option == 2:
            self.create_account()
        elif option == 3:
            self.search()
        elif option ==5:
            self.play_video()
        elif option == 5:
            Menu.MainMenu().exit()
        else:
            print(f"{option} is not supported. Please try again")
            self.menu()

    def sign_in(self):
        print("** Sign-In **")
        username = input("Username: ")
        password = input("Password: ")

        user = db.get_user(username)

        if user is None:
            print(f"\nUnfortunately, no user was found with the username {username}.\n")
            print("\nPlease Create Account or try Signing in with existing credentials.\n")
            self.menu()
        elif password != user[1]:
            print(f"\nInvalid Password. Please create an account or attempt signing in again.\n")
            self.menu()
        else:
            print(f"\nWelcome {username}! Sending you to the main menu navigation.\n")
            Menu.MainMenu().main_menu_options()

    def create_account(self):
        num_of_users = db.count_users()
        if num_of_users >= 5:
            print("\n** WARNING **")
            print("We are not creating new accounts at this time. Please Sign in to existing account\n")
            return self.menu()

        print("** Create Account **")
        username = input("Username: ")

        user = db.get_user(username)
        if user is not None:
            print("\nSorry, this account already exists. Please try again\n")
            return self.menu()
        '''
        print("\nPassword Requirements:")
        print("- Length cannot exceed 12. Length is greater than 7")
        print("- Must include and uppercase letter")
        print("- Must include a special character")
        print("- Must include numbers")
        '''
        password = input("Password: ")

        while True:
            if len(password) < 8 or len(password) > 12:
                print("\nInvalid password please try again: ")
                password = input("")
            elif not re.search(r'[A-Z]', password) or not re.search(r'\d', password) or not re.search(r'[ -\/:-@\[-`{-~]', password):
                print("\nInvalid password please try again: ")
                password = input("")
            else:
                first_name = input("First name: ")
                last_name = input("Last name: ")
                while True:
                    check = db.check_name(first_name.lower(), last_name.lower())
                    if check:
                        print("This person already exists in our system. Please make a new name.")
                        first_name = input("First name:")
                        last_name = input("Last name: ")
                    else:
                        break
                db.add_user(username, password, first_name.lower(), last_name.lower())
                print(f"\nWelcome {username}! Sending you to the main menu navigation.\n")
                break

        Menu.MainMenu().main_menu_options()

    def play_video(self):
        print("Video is now playing")

    def search(self):
        print("\nWould you like to search for someone you know?")
        print("1.) Yes ")
        print("2.) No return to previous")

        choice = int(input("Please enter 1 or 2: "))
        while True:
                if choice != 1 and choice !=2:
                    choice = int(input("Invalid input please enter 1 or 2: "))
                else:
                    break
        
        if choice == 1:
            first_name = input("\nPlease enter their first name: ")
            last_name = input("Please enter their last name: ")
            user = db.check_name(first_name.lower(), last_name.lower())
            if user:
                print("\nThey are part of the InCollege system\n")
                print("Would you like to join your friends on InCollege\n")
                print("1.) Yes I would like to login or sign up")
                print("2.) No Return to previous page")
                opt = int(input("Please enter 1 or 2: "))
                while True:
                        if opt != 1 and opt !=2:
                            opt = int(input("Invalid input please enter 1 or 2: "))
                        else:
                            break
                if opt == 1:
                    print("1.) Sign In")
                    print("2.) Create Account")
                    print("3.) Return to previous page")
                    option = int(input("Enter option: "))
                    while True:
                        if option != 1 and option !=2 and option != 3:
                            option = int(input("Invalid input please enter 1, 2, or 3: "))
                        else:
                            break
                    if option == 1:
                        self.sign_in()
                    elif option == 2:
                        self.create_account()
                    elif option == 3:
                        self.search()

                    
                elif opt == 2:
                    return self.search()
            else:
                print("\nThey are not yet a part of the InCollege system yet\n")
                return self.search()
        
        elif choice == 2:
            return self.menu()
        