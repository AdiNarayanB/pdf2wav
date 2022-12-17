from PyPDF2 import PdfReader
from TTS.api import TTS
import base64
import typing


class pdf2wavServer:
    def __init__(self, docFmt, audioFmt, responseType, pdfFilePath):
        self.docFmt = docFmt
        self.audioFmt = audioFmt
        self.responseType = responseType
        self.pdfFilePath = pdfFilePath
        self.wavFilePath = self.pdfFilePath + ".wav"

    def getTextFromPdf(self) -> str:
        pdfObj = PdfReader(self.pdfFilePath)

        page_text = ""
        for page in pdfObj.pages:
            page_text += page.extractText()
        text = page_text
        return text

    def getWavFromText(self, transcript: str):
        model_name = TTS.list_models()[0]

        tts = TTS(model_name)
        filepath = self.pdfFilePath + ".wav"

        tts.tts_to_file(text=transcript, speaker=tts.speakers[1], language=tts.languages[0],
                        file_path=filepath)

    # Running a single speaker model

    # Init TTS with the target model name

    # Run TTS
    def cvtPdfToWav(self):
        import os

        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        print(files)
        print(os.getcwd())
        text = self.getTextFromPdf()
        self.getWavFromText(text)

    def dumpFile(self) -> typing.Dict[str, str]:
        response = {}
        with open(self.wavFilePath, "rb") as f:
            response['content'] = base64.b64encode(f.read()).decode("utf8")
        return response

    def executePdfToWav(self):
        self.cvtPdfToWav()
        response = self.dumpFile()
        return response
