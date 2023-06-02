# Imports
from Util import db_helper as db


class SkillsPage:
    @staticmethod
    def select_skill():
        print("Please Select a Skill")
        print("1.) Communication")
        print("2.) Project Management")
        print("3.) Teamwork")
        print("4.) Organization")
        print("5.) Problem Solving")
        print("\n6.) Exit")
        while True:
            choice = int(input("Please enter a skill you would like to work on: "))
            if choice >= 1 and choice <= 5:
                print("under construction")
            elif choice == 6:
                print("Going back to main menu")
                return
            else:
                print("Please enter a valid response")