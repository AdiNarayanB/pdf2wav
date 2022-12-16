import requests


def pdf2wavConverter(pdfFilePath: str, wavFilePath: str, queryURL: str) -> bool:
    try:
        with open(pdfFilePath, 'rb') as f:
            resp = requests.post(queryURL, files={'file': f})
        with open(wavFilePath, "wb") as file:
            file.write(resp.content)
        return True
    except Exception as e:
        print(e)
        print("PDF conversion to wav file failed!")
        return False
