# Import Section
from Util import db_helper as db
import MainMenu as Menu


class ConnectionsPage:
    def __init__(self):
        self.menu = Menu.MainMenu()

    def load_connections(self):
        print("\n** Connect To Your Peers **\n")
        print("1.) Find Connection")
        print("2.) Return to Menu")
        print("4.) Exit\n")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            self.find_user()
        elif choice == 2:
            self.menu.main_menu_options()
        elif choice == 4:
            Menu.MainMenu.exit()
        else:
            print()

    def find_user(self):
        query = input("Search for User (first and last name): ")
        name = query.split()
        returned_user = db.get_user_by_name(name[0], name[1])
        if returned_user is None:
            print("They are not part of the InCollege System")
            self.load_connections()
        else:
            print("They are part of the InCollege System")
            self.load_connections()
