
import requests
import base64

class pdf2wavClient:
    def __init__(self, pdfFilePath, wavFilePath, queryURL):
        self.pdfFilePath = pdfFilePath
        self.wavFilePath = wavFilePath
        self.queryURL = queryURL
    def pdf2wavConverter(self):
        with open(self.pdfFilePath, 'rb') as f:
            resp = requests.post(self.queryURL, files={'file': f})
        with open(self.wavFilePath,"wb") as f:
            f.write(base64.b64decode(resp.json()['content']))
        return True





