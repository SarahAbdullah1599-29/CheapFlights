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
        