
# PDF2Wav

Note: This Project is a work in progress. Help is appreciated! Look at the contributing section to look at some features that could be worked on!


A simple Flask based REST API for converting text contained in PDF's to freeform speech using a TTS API, with some extra emphasis on using design patterns, and decoupling business logic whenever possible. 








## Badges

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)


## Authors

- [@adiraokhoury](https://www.github.com/adiraokhoury)


## Contributing

Contributions are always welcome!
Features Requests are tracked in [this](https://github.com/users/adiraokhoury/projects/1) github project board. 



## Blog Post


The internals of why and how I built this is detailed in my [blog post](https://adiraokhoury.github.io/blogPost1.html) on my [website](https://adiraokhoury.github.io). 


## Setup and Installation

1.Installing the requirements:


```
cd server
pip3 install requirements.txt
```

2.Setup the Servers:

Setting up Redis:

```
redis-server
```

Setting up API endpoints:

```
cd server
gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:app 
```







3.Adhoc Testing:

Testing with pytest:

Navigate to the client folder and run ```pytest```. Tests are still a heavy WIP. 

Trying it yourself:

i) Navigate to the client folder.

ii) Then run the generateToken utlity from cli.py, that will get you the credentials you need to work with the API. 
```
python3.8  cli.py generatetoken --username asdf --password qwerty

```
This generates a file called ```tokens.json``` . Make sure cli.py and tokens.json lie in the same directory. 

iii) Now, run the pdf2wav utility, that will take a pdf path and a file path that youd want to save your transcription in. 

```
python3.8  cli.py generatewavfrompdf --pdffilepath /home/adithya/Desktop/AdithyaNarayan-6.pdf --wavfilesavepath /home/adithya/testRecordingFINAL.wav
```

## API Routes

Supported API Routes at the moment and how to work with them

```
/register

Description: Identifies a user and generates a token for using the pdf2wav service.
Input: Json String of the form {'username': STRING, 'password':STRING}

Output: Json String of the form {"password":"gnjgjgjgj","token":"63D24NG679OG5BE","username":"my_login"}
cURL command: curl -X POST http://0.0.0.0:5000/register -H 'Content-Type: application/json' -d '{"username":"my_login","password":"gnjgjgjgj"}'
```

```
/pdf2wav

Description: Converts a pdf encoded as bytes into a wav file with the transcription.
Input: Json String of the form {'username':STRING, 'token': STRING, 'data': BYTES}

Output: 
If token passed is invalid/expired: Json String of the form {"error":"Token Not Found"}

If token passed is valid: Json String of the form {'content': BYTES}

cURL command: TBD
requests command: requests.post(self.queryURL, json = {'username':tokenUsername,'token':tokenHash,'data':base64.b64encode(f.read()) }, headers = {"Content-Type":"application/json"})

NOTE: Using the CLI to communicate with /pdf2wav ensures that the credentials needed to communicate with the API are loaded through the tokens.json and not manually. 

```
## Lessons Learned



Flask is NOT a reliable web server. Nginx and Gunicorn make flask capable of handling high traffic. 

Dependency Inversion and Injection in Python is very easy to violate due to a lack of type checking. Using a plugin like [mypy](https://mypy.readthedocs.io/en/stable/index.html) can help mitigate this. 

There aren't a lot of experiments done on Reading and Writing wav files from/to different cache implementations. From this perspective, I do think that repurposing this project as a tool for analyzing bulk R/W performance of multimedia on different storage implementations(S3, NFS, Redis, etc) might be a future avenue for improvement. 

## Some avenues for improvement

1. Brute force username and token passing to the ```/pdf2wav``` endpoint:

It is definetly possible to randomly generate various combinations of letters and numbers, for both the username and token fields, and eventually bypass authentication. 

A workaround here would be to maintain a seperate key value store within redis such that each ip address has only a set number of invalid token errors that can be returned to the user in question. If this number drops to 0, users could be added to a blacklist that tells the API who to block the service for entirely. 

An alternate approach could be to use something more fully fledged, like JWT or OAuth. 

2. File Saving vs Byte Array Response:

On retrieving the byte array from the request object, passing it the PDFReader Object and obtaining the text is a better option as compared to saving the PDF Byte Array into a PDF file locally and loading it once more through the PDFReader API. This has to do with minimizing how much space each request occupies. Using the same philosophy when running TTS on the obtained text, we want to be able to load the transciption byte array into a response object directly instead of saving the file and the loading it once more. This would require isolating a part of the TTS functionality so that it returns the waveform array directly isntead of saving it locally. 



