from clientPdf2Wav import pdf2wavClient


if __name__ == "__main__":
    pdfFilePath = "/home/adithya/Desktop/AdithyaNarayan-5.pdf"
    wavFilePath = "/home/adithya/testRecording.wav"
    queryURL = 'http://127.0.0.1:5000/pdf2wav'
    pdf2wavClientObj = pdf2wavClient(pdfFilePath, wavFilePath, queryURL)
    pdf2wavClientObj.pdf2wavConverter()
