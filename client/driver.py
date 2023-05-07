from clientPdf2Wav import pdf2wavClient


if __name__ == "__main__":

    pdfFilePath = ""
    wavFilePath = ""
    queryURL = ''

    pdf2wavClientObj = pdf2wavClient(pdfFilePath, wavFilePath, queryURL)

    pdf2wavClientObj.pdf2wavConverter()

