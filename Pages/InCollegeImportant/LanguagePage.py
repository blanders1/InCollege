from Util import db_helper as db
from Pages import LoginPage as login


class LanguagePage:

    def menu(self):
        if login.username == "":
            print("\nPlease login before trying to edit language settings\n")
            return

        print("\n* Language *\n")
        print("Set Language:")
        print("1.) English")
        print("2.) Spanish")
        print("0.) Return")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            db.change_language(db.get_user(login.username)[0], "English")
        elif choice == 2:
            db.change_language(db.get_user(login.username)[0], "Spanish")
        elif choice == 0:
            return
