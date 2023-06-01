# Imports
from Util import db_helper as db


class SkillsPage:
    @staticmethod
    def select_skill():
        print("Please Select a Skill")
        print("1.) ")
        print("2.) ")
        print("3.) ")
        print("4.) ")
        print("5.) ")
        choice = int(input("Please enter a skill you would like to work on: "))