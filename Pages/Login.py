

class Login:
    def menu(self):
        print("Please Login: ")
        print("1.) Sign In")
        print("2.) Create Account")
        option = int(input("Enter Option: "))
        if option == 1:
            self.sign_in()
        elif option == 2:
            self.create_account()
        else:
            print(f"{option} is not supported. Please try again")
            self.menu()

    def sign_in(self):
        return

    def create_account(self):
        return