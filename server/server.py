from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from serverPdf2Wav import pdf2wavServer
from cache.cache import RedisCache
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
def extractwav():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()

    elif request.method == 'POST':
        try:

            f = request.files['file']
            file_name = f.filename
            save_path = "tmp_files/" + file_name
            f.save(save_path)
            redisObj = RedisCache("127.0.0.1")

            pdf2wavServerobj = pdf2wavServer("pdf", "wav", "bytes", save_path,redisObj)

            response = pdf2wavServerobj.executePdfToWav()

            return response
        except Exception as e:
            return jsonify(e)
    else:
        return jsonify("server only allows POST")


if __name__ == "__main__":
    app.run(debug=True)
