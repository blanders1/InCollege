# Imports
from Util import db_helper as db
import MainMenu as menu
from Pages.skills import Skills1Page as skill1
from Pages.skills import Skills2Page as skill2
from Pages.skills import Skills3Page as skill3
from Pages.skills import Skills4Page as skill4
from Pages.skills import Skills5Page as skill5


class SkillsPage:
    @staticmethod
    def select_skill():
        print("Please Select a Skill")
        print("1.) Skill 1")
        print("2.) Skill 2")
        print("3.) Skill 3")
        print("4.) Skill 4")
        print("5.) Skill 5")
        print("9.) Main Menu")
        choice = int(input("Please enter a skill you would like to work on: "))

        if choice == 1:
            skill1.Skills1Page.load_skill_1()
        elif choice == 2:
            skill2.Skills2Page.load_skill_2()
        elif choice == 3:
            skill3.Skills3Page.load_skill_3()
        elif choice == 4:
            skill4.Skills4Page.load_skill_4()
        elif choice == 5:
            skill5.Skills5Page.load_skill_5()
        elif choice == 9:
            return menu.MainMenu.main_menu_options
        else:
            print("Please try again \n")
            SkillsPage.select_skill()



