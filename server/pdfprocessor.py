import codecs

from PyPDF2 import PdfReader
from TTS.api import TTS
from flask import Flask, request, jsonify, make_response,send_file
from flask_cors import CORS

import base64
import json
def getTextFromPdf(pdfFilePath: str) -> str:
    pdfObj = PdfReader(pdfFilePath)

    page_text = ""
    for page in pdfObj.pages:
        page_text += page.extractText()
    text = page_text
    return text


def getWavFromText(transcript: str, filename: str) -> str:
    model_name = TTS.list_models()[0]

    tts = TTS(model_name)
    filepath = filename+".wav"



    tts.tts_to_file(text=transcript, speaker=tts.speakers[1], language=tts.languages[0],
                    file_path=filepath)

    return filepath


# Running a single speaker model

# Init TTS with the target model name

# Run TTS
def cvtPdfToWav(pdfFileName: str) -> str:
    import os
    import sys
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(files)
    print(os.getcwd())
    text = getTextFromPdf(pdfFileName)
    wavFilePath = getWavFromText(text, pdfFileName)
    return wavFilePath


application = app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = ['.docx', '.doc', '.txt', '.pdf', '.html']
cors = CORS(app)


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route('/')
@app.route('/pdf2wav', methods=['POST', 'OPTIONS'])
def extractext():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()

    elif request.method == 'POST':
        try:

            f = request.files['file']
            file_name = f.filename

            print(file_name)
            f.save("tmp_files/"+file_name)


            wavFilePath = cvtPdfToWav("tmp_files/"+file_name)
            response = {}
            with open(wavFilePath,"rb") as f:
                        response['content'] = base64.b64encode(f.read()).decode("utf8")
            return response
            #return send_file(wavFilePath,'audio/wav')

        except Exception as e:
            return jsonify(e)
    else:
        return jsonify("server only allows POST")


if __name__ == "__main__":

    app.run(debug=True)
