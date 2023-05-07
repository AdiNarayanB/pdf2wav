
import requests
import base64
import json

class pdf2wavClient:
    def __init__(self, pdfFilePath, wavFilePath, queryURL,tokenUsername, tokenPassword, tokenHash):
        self.pdfFilePath = pdfFilePath
        self.wavFilePath = wavFilePath
        self.queryURL = queryURL
        self.tokenUsername = tokenUsername
        self.tokenPassword = tokenPassword
        self.tokenHash = tokenHash








    def pdf2wavConverter(self):



        with open(self.pdfFilePath, 'rb') as f:

            resp = requests.post(self.queryURL, json = {'username':self.tokenUsername,'token':self.tokenHash,'data':base64.b64encode(f.read()) }, headers = {"Content-Type":"application/json"})



        if "TokenNotFound" in resp.json().keys():
              print ({"error":"Token Not Found"})
              return False
        else:
            with open(self.wavFilePath,"wb") as f:
                        f.write(base64.b64decode(resp.json()['content']))
        return True







