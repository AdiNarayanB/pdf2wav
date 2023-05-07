
import sys, os

# Disable

import base64
import io
import PyPDF2
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from serverPdf2Wav import pdf2wavServer
from cache.cache import RedisCache
import random
import ast
import string
import json


application = app = Flask(__name__)
UserRegisterDB = RedisCache("127.0.0.1:6379")

app.config['UPLOAD_EXTENSIONS'] = ['.docx', '.doc', '.txt', '.pdf', '.html']
cors = CORS(app)


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route('/')
@app.route('/register',methods=['POST'])
def register():
        if request.method == "POST":
                print(request.json)
                try:
                        username = request.json['username']
                        password = request.json['password']


                        token = UserRegisterDB.put(username,password)
                        return {"username":username ,"password":password,"token":token}

                except Exception as e:
                    print (e)
                    return jsonify(e)


def randomStringHash(N:int) -> str:

        sHash = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
        return sHash



@app.route('/pdf2wav', methods=['POST', 'OPTIONS'])
def extractwav():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()

    elif request.method == 'POST':


        try:





            username, token = request.json['username'], request.json['token']





            is_registered = UserRegisterDB.validateToken(username, token)
            if not is_registered:

                    return {"TokenNotFound":token}

            fPath = "tmp_files/"+randomStringHash(10)+".wav"



            pdfObj = PyPDF2.PdfFileReader(io.BytesIO(base64.b64decode(request.json['data'])))

            #Facade

            pdf2wavServerobj = pdf2wavServer("pdf", "wav", "bytes", pdfObj,RedisCache("127.0.0.1:6379"),fPath)

            response = pdf2wavServerobj.executePdfToWav()

            return response
        except Exception as e:
            print (e)
            return jsonify(e)
    else:
        return jsonify("server only allows POST")


if __name__ == "__main__":
    app.run(debug=True)
