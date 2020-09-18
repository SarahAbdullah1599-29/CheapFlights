from account import Account
from search_flight import SearchFlights
import json

class Sign_In_Page:

    def __init__(self, account, account_list):
        self.account = account
        self.account_list = account_list

    def save(self):
        with open("accounts.json", "w") as accounts_json:
            serilizated_data = self.serilization()
            json.dump(serilizated_data, accounts_json,sort_keys=True, indent=4)

    def serilization(self):
        exeList=[]
        for i in range(len(self.accountList)):
            serilizated = {}
            serilizated["username"] = self.accountList[i].username
            serilizated["password"] = self.accountList[i].password
            serilizated["email"] = self.accountList[i].email
            serilizated["flights"] = self.accountList[i].flights
            exeList.append(serilizated)
        return exeList

    def display_options(self):  
        print(f""" 
             Hi {self.account.username}, you've successfully signed in! 
             Please choose one of the options below:
 
             1. Search Flights
             2. Show Saved Flights
             3. Change Username
             4. Change email address
             5. Change password
             6. Delete account
             Q. Sign Out
             """)

    def search_flight(self, search):
        flight = search_flight(search)
        return flight.flight.link    

    def update_account(self, new_username, new_password, new_email):
        for acc in self.account_list:
            if acc.username == new_username:
                return (True, None)
        else:
            self.account.username = new_username
            self.account.password = new_password
            self.account.email = new_email
            return (False, self.account)

    def delete_account(self):
        for i in range(len(self.account_list)):
            if self.account_list[i].username == self.account.username:
               self.account_list.pop(i)
               return True
        else:
            return False

    def run(self):
        while True:
            #self.display_options()  
            option = input("Enter an option: ")
            if option.lower() == "q":
                break

            action = self.options.get(option)
            if action:
                return_statement = action()
                if return_statement == False:
                    break
            else:
                print("{0} is not a valid option, please try again!".format(option))
 