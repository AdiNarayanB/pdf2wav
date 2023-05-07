
import requests
import base64
import json


class pdf2wavRegister:
    def __init__(self, queryURL,tokenUsername, tokenPassword):

        self.queryURL = queryURL

        self.tokenUsername = tokenUsername
        self.tokenPassword = tokenPassword



    def getToken(self):





        resp = requests.post(self.queryURL, json = {'username':self.tokenUsername,'password':self.tokenPassword}, headers = {"Content-Type":"application/json"})

        with open("tokens.json", "w") as f:
            json.dump(resp.json(),f)