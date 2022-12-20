from PyPDF2 import PdfReader
from TTS.api import TTS
import base64
import typing


class pdf2wavServer:
    def __init__(self, docFmt, audioFmt, responseType, pdfFilePath,cacheObj):
        self.docFmt = docFmt
        self.audioFmt = audioFmt
        self.responseType = responseType
        self.pdfFilePath = pdfFilePath
        self.wavFilePath = self.pdfFilePath + ".wav"
        self.wavObj = None
        self.cache = cacheObj
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

        wav = tts.tts(text=transcript, speaker=tts.speakers[1], language=tts.languages[0])
        cacheHitObj = self.cache.fromRedis(filepath)

        if cacheHitObj is None:
            self.cache.put(wav,filepath)

        else:
            return cacheHitObj
    # Running a single speaker model

    # Init TTS with the target model name

    # Run TTS
    def cvtPdfToWav(self):
        import os

        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        print(files)
        print(os.getcwd())
        text = self.getTextFromPdf()
        wavObj = self.getWavFromText(text)
        self.wavObj = wavObj

    def dumpFile(self) -> typing.Dict[str, str]:
        response = {}


        response['content'] = base64.b64encode(self.wavObj).decode("utf8")
        return response

    def executePdfToWav(self):
        self.cvtPdfToWav()
        response = self.dumpFile()
        return response
