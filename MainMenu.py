from Pages import LoadProfile
from Pages import LoadConnections
from Pages import LoadJobOpportunities

# Comment to see if pushing is working
class MainMenu:
    @staticmethod
    def invalid_response(self, invalid_selection):
        print(f"{invalid_selection} is not a valid option. Please only enter the number")
        print("next to the option you would like to navigate to.")
        MainMenu.main_menu_options()

    @staticmethod
    def selected_menu_option(self, i):
        switcher = {
            1: LoadProfile.load_profile(),
            2: LoadConnections.load_connections(),
            3: LoadJobOpportunities.load_job_opportunities(),
        }
        return switcher.get(i, MainMenu.invalid_response(i));

    @staticmethod
    def main_menu_options(self):
        print("1.) Your Profile")
        print("2.) Your Connections")
        print("3.) Job Opportunities")
        choice = input("\nPlease enter where you would like to navigate: ")
        MainMenu.selected_menu_option(choice)
