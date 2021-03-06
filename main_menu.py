from application import Application

class Main_Menu:

    def __init__(self):
        self.app = Application()
        self.app.load()
        self.options = {
            "1.": self.app.sign_up,
            "2.": self.app.sign_in,
        }
    
    def display_options(self):
        print(""" 
            ************* MAIN MENU *************
             Welcome to CheapFlights! 
             Please choose one of the options below:
 
             1. Create an account
             2. Sign in to your account
             Q. Quit
             """)
    def run(self):
        while True:
            self.display_options()
            option = input("Enter an option: ")
            if option.lower() == "q":
                print("JSON file has been saved to account.json file")
                self.app.save()
                break

            action = self.options.get(option)
            if action:
                action()
            else:
                print("{0} is not a valid option, please try again!".format(option))         