# Imported Libraries

# Imported Files
import MainMenu as Menu

# Main loop, so application persists while in use

print("##################################################")
print("# Welcome to inCollege Command Line Environment  #")
print("#                                                #")
print("#        Developed By Team: New Mexico           #")
print("##################################################")
print("")

is_application_in_use = True
user_interface = Menu.MainMenu()

while is_application_in_use:
    is_application_in_use = user_interface.main_menu_options()


print()
print("##################################################")
print("#                                                #")
print("#        Thank you for using inCollege           #")
print("#                                                #")
print("##################################################")

