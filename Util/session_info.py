
class SessionInfo:

    def __init__(self):
        self.name = "Anonymous"
        self.email = "No Current Email"
        self.phone = "No Current Phone"

    def set_current_user(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def get_current_user(self, name):
        print("")