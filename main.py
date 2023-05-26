# Imported Libraries
import sys
import os

# Imported Files
import MainMenu

# Main loop, so application persists while in use

is_application_in_use = True
while(is_application_in_use):
    print("##################################################")
    print("# Welcome to inCollege Command Line Environment  #")
    print("#                                                #")
    print("#        Developed By Team: New Mexico           #")
    print("##################################################")

    MainMenu.main_menu_options()

