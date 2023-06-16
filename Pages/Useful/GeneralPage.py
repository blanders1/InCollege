from Pages.Useful.General import AboutPage as About, HelpCenterPage as Help, PressPage as Press, BlogPage as Blog, \
    CareersPage as Career, DevelopmentPage as Developer
from Pages import LoginPage

class GeneralPage:

    def menu(self):
        print("\n** General Links **\n")
        print("1.) Sign Up")
        print("2.) Help Center")
        print("3.) About")
        print("4.) Press")
        print("5.) Blog")
        print("6.) Careers")
        print("7.) Developers")
        print("0.) Return To Menu")

        choice = int(input("Enter Option: "))


        if choice == 1:
            LoginPage.Login().menu()
        elif choice == 2:
            Help.HelpCenterPage().menu()
        elif choice == 3:
            About.AboutPage().menu()
        elif choice == 4:
            Press.PressPage().menu()
        elif choice == 5:
            Blog.BlogPage().menu()
        elif choice == 6:
            Career.CareersPage().menu()
        elif choice == 7:
            Developer.DeveloperPage().menu()
        elif choice == 0:
            return
        else:
            self.menu()

