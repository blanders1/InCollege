from Util import db_helper as db
from Util import session_info as account
import MainMenu as Menu
import re


class Login:
    def menu(self):
        print("Please Login: ")
        print("1.) Sign In")
        print("2.) Create Account")
        option = int(input("Enter Option: "))
        if option == 1:
            self.sign_in()
        elif option == 2:
            self.create_account()
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
            self.menu()

        print("** Create Account **")
        username = input("Username: ")

        user = db.get_user(username)
        if user is not None:
            print("\nSorry, this account already exists. Please try again\n")
            self.menu()

        print("\nPassword Requirements:")
        print("- Length cannot exceed 12. Length is greater than 7")
        print("- Must include and uppercase letter")
        print("- Must include a special character")
        print("- Must include numbers")
        password = input("Password: ")

        while True:
            if len(password) < 8 or len(password) > 12:
                password = input("Invalid password please try again: ")
            elif not re.search(r'[A-Z]', password) or not re.search(r'\d', password) or not re.search(r'[ -\/:-@\[-`{-~]', password):
                password = input("Invalid password please try again: ")
            else:
                db.add_user(username, password)
                print("\nYour new account has been created thank you")
                print("Try logging in\n")
                self.sign_in()
