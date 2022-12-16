import requests


def pdf2wavConverter(pdfFilePath: str, wavFilePath: str, queryURL: str) -> bool:
    try:
        req = {}
        with open(pdfFilePath, 'rb') as f:
            req['content'] = f
            req['file_name'] = pdfFilePath
            resp = requests.post(queryURL, req)
        with open(wavFilePath, "wb") as file:
            file.write(resp.content)
        return True
    except Exception as e:
        print(e)
        print("PDF conversion to wav file failed!")
        return False



isSuccess = pdf2wavConverter("/home/adithya/Desktop/project proposal(1).pdf","/home/adithya/testRecording.wav",'http://127.0.0.1:5000/pdf2wav')
print(isSuccess)


