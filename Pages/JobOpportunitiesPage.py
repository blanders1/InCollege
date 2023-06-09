# Imports
from Util import db_helper as db
import MainMenu as menu

class JobOpportunitiesPage:
    @staticmethod
    def load_job_opportunities():
        print("1.) Post a job")
        print("9.) Main menu")
        choice = int(input("Please enter a skill you would like to work on: "))
        if choice == 1:
            self.post_job()
        elif choice == 9:
            return menu.MainMenu.main_menu_options
    def post_job(self):
        print ("under construction")