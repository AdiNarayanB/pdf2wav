from PyPDF2 import PdfReader
from TTS.api import TTS
import os
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS


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

    tts.tts_to_file(text=transcript, speaker=tts.speakers[1], language=tts.languages[0],
                    file_path="/" + filename + "_" + "speech.wav")

    return filename + "_" + "speech.wav"


# Running a single speaker model

# Init TTS with the target model name

# Run TTS
def cvtPdfToWav(pdfFileName: str) -> str:
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

            save_path = os.path.join(
                app.config.get('upload_folder'), file_name)
            f.save(save_path)
            wavFilePath = cvtPdfToWav(file_name)
            response = {}
            with open(wavFilePath, "rb") as wavContent:
                response["content"] = wavContent

            return response
        except Exception as e:
            return jsonify(e)
    else:
        return jsonify("server only allows POST")


if __name__ == "__main__":
    app.run(debug=True)
