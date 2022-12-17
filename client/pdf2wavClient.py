import base64

import requests


def pdf2wavConverter(pdfFilePath: str, wavFilePath: str, queryURL: str) -> bool:


        with open(pdfFilePath, 'rb') as f:
            resp = requests.post(queryURL, files={'file': f})
        with open(wavFilePath,"wb") as f:
            f.write(base64.b64decode(resp.json()['content']))

        return True




isSuccess = pdf2wavConverter("/home/adithya/Desktop/AdithyaNarayan-5.pdf","/home/adithya/testRecording.wav",'http://127.0.0.1:5000/pdf2wav')
print(isSuccess)


