# Imports
from Util import db_helper as db
import MainMenu as Menu


class JobOpportunitiesPage:

    def load_job_opportunities(self):
        print("\n** Your Job Prospects and Opportunities **\n")
        print("1.) Post Job")
        print("2.) Return to Menu")
        print("4.) Exit")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            self.post_job()
        elif choice == 2:
            Menu.MainMenu().main_menu_options()
        elif choice == 4:
            Menu.MainMenu().exit()
        else:
            print("Invalid Option")
            self.load_job_opportunities()

    def post_job(self):
        num_of_jobs = db.count_jobs()
        if num_of_jobs >= 5:
            print("\n** WARNING **")
            print("We are not creating new jobs at this time.\n")
            return self.load_job_opportunities()

        print("\nPost your job: ")
        title = input("Position Title: ")
        description = input("Description of Role: ")
        employer = input("Who is the employer: ")
        location = input("Where is position located: ")
        salary = int(input("What is the salary of the position: "))
        user = db.get_current_user()

        db.add_job(title, description, employer, location, salary, user[0])
        print("Job Added")
        self.load_job_opportunities()
