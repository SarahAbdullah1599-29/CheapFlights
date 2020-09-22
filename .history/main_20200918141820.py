from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin

from application import Application
from sign_in_page import Sign_In_Page

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/sign-up', methods=['POST'])
@ cross_origin()
def sign_up():
    #have to create a front end to request the data
    data = request.get_json()
    username, password, email = data["username"], data["password"], data["email"]
    account_existed = project.sign_up(username, password, email)
    if account_existed:
        return {"message":"An account with the username and/or email already exists, please try again!"}, 400 #error
    else:
        project.save()
        return {"message":"Congratulations, you've successfully created an account"}, 200 #good
@app.route('/search-flights', methods=['POST'])
@ cross_origin()
def search_flight():
    data = request.get_json()
    username, password, search_term = data["username"], data["password"], data["searchTerm"]
    account_not_found, user_data = project.sign_in(username, password)
    
    if account_not_found:
        return {"message":"The username of the password you've entered in incorrect, please try again"}, 400 #error
    else:
        sign_in = Sign_In_Page(user_data,project.accountDict)
        search_result = sign_in.search_flight(search_term)

        if len(search_result) > 0:
            return {"message": "No flights available to this destination": search_result } ,200
        else:
            return {"message": "No Flights Available"}, 400        