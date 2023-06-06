from PyPDF2 import PdfReader
from TTS.api import TTS
import base64
import typing


class pdf2wavServer:
    def __init__(self, docFmt, audioFmt, responseType, pdfObj,cacheObj,clientWavPath):
        self.docFmt = docFmt
        self.audioFmt = audioFmt
        self.cacheObj = cacheObj
        self.responseType = responseType
        self.clientWavPath = clientWavPath
        self.pdfObj = pdfObj

        self.wavObj = None

    def getTextFromPdf(self) -> str:


        page_text = ""
        for page in self.pdfObj.pages:
            page_text += page.extractText()
        text = page_text
        return text

    def getWavFromText(self, transcript: str) -> bytes:
        model_name = TTS.list_models()[0]

        tts = TTS(model_name)
        filepath = self.clientWavPath

        wav = tts.tts_to_file(text=transcript, speaker=tts.speakers[1], language=tts.languages[0],file_path=filepath)

        with open(filepath,"rb") as f:
                bytes = f.read()
        return bytes

    # Running a single speaker model

    # Init TTS with the target model name

    # Run TTS
    def cvtPdfToWav(self) -> None:
        import os

        files = [f for f in os.listdir('.') if os.path.isfile(f)]

        text = self.getTextFromPdf()
        wavObj = self.getWavFromText(text)
        self.wavObj = wavObj

    def dumpFile(self) -> typing.Dict[str, str]:
        response = {}

        response['content'] = base64.b64encode(self.wavObj).decode("utf8")
        return response

    def executePdfToWav(self) -> dict:

        self.cvtPdfToWav()
        response = self.dumpFile()
        return response
