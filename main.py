# Imported Libraries

# Imported Files
import MainMenu as Menu
from Pages import LoginPage as Login


exit_screen = Menu.MainMenu()
print("##################################################")
print("# Welcome to inCollege Command Line Environment  #")
print("#                                                #")
print("#        Developed By Team: New Mexico           #")
print("##################################################")
print("")

print("Here's one of our success stories: ")
print("")
print("1.) To Learn More")
print("2.) To Login")
print("4.) Exit")
choice = int(input("Navigate To: "))

if choice == 1:
    print("Watch this video")
elif choice == 2:
    is_application_in_use = True
    login_interface = Login.Login()

    while is_application_in_use:
        is_application_in_use = login_interface.menu()
    exit_screen.exit()

elif choice == 4:
    exit_screen.exit()
else:
    print("Invalid Option")


