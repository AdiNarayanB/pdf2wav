


import pytest
import json
from clientPdf2Wav import pdf2wavClient
from clientPdf2WavRegister import pdf2wavRegister

def testGenerateToken():
    username = "FJFJFJ"
    password =  "ERGI8OERIOGER"

    flag = 0

    registerObj = pdf2wavRegister('http://0.0.0.0:5000/register', username, password)

    registerObj.getToken()
    with open("tokens.json","r") as f:
        vals = json.load(f)
        if "token" in vals.keys():
            flag = 1
    assert flag == 1



def testTokenLength16():
    with open("tokens.json","r") as f:
        tokenVals = json.load(f)
        tokenHash = tokenVals['token']
    assert len(tokenHash) == 15



def testTokenLengthNot16():
    tokenHash = "5348094548"

    assert len(tokenHash) != 15











