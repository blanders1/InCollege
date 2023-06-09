# Import Section
from Util import db_helper as db
import MainMenu as menu


class ConnectionsPage:
    @staticmethod
    def load_connections():
        print("Would you like to find a connection with someone you know?")
        print("1.) Yes ")
        print("2.) No return to previous")

        choice = int(input("Please enter 1 or 2: "))
        print("\n")
        if choice == 1:
            first_name = input("Please enter their first name: ")
            last_name = input("Please enter their last name: ")
            user = db.check_name(first_name.lower(), last_name.lower())
            if user:
                print("They are part of the InCollege system\n")
            else:
                print("They are not yet a part of the InCollege system yet\n")
        
        elif choice == 2:
            return menu.MainMenu.main_menu_options
