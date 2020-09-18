import json
import requests

class SearchFlights:
    def __init__(self,name):

        name = name.lower()
        api_key = "61cd34f870msha7e741f51fc35a6p16eac5jsn31585c0320b3"
        url = "https://tripadvisor1.p.rapidapi.com/answers/list"
        search_param = {"query": name, "per_page": "12"} #to show the name of 12 different airlines flight options
        headers = {"Authorization": api_key}
        try:
            response = response.get(url,params=search_param,headers=headers)
            data = response.json()
    
    def __str__(self):
        return f"this is the cheapest flights available:{}"
        