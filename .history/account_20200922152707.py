import json

class Account():
    def __init__(self,username,password,email,flight=[]):
        self.username = username
        self.password = password
        self.email = email
        self.flight = flight

    @classmethod
    def from_json(cls,data):
        username,password,email,flight =  data ["username"],data["password"],data ["email"],data["flight"]
        return cls(username=username, password=password, email=email, flight=flight)

    def __str__(self):
         return f"this is username: {self.username}\nthis is password: {self.password}\nthis is email: {self.email}\nthis is flight: {self.flight}"
