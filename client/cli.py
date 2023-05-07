import click
from clientPdf2Wav import pdf2wavClient
from clientPdf2WavRegister import pdf2wavRegister
import json



@click.group()
def cli():
        pass


@click.command()

@click.option('--username', help = 'Choose an username')
@click.option('--password', help = 'Choose a password')



def generateToken(username, password):
    print (username,password)

    registerObj = pdf2wavRegister('http://0.0.0.0:5000/register', username, password)
    registerObj.getToken()




@click.command()

@click.option('--pdffilepath', help = ' PDF file path saved locally ' )
@click.option('--wavfilesavepath', help = 'Path to save result WAV file locally')



def generateWavFromPdf(pdffilepath,wavfilesavepath):
    with open("tokens.json","r") as f:
            vals = json.load(f)
            token = vals['token']
            username = vals['username']
            password = vals['password']
    clientObj = pdf2wavClient(pdffilepath, wavfilesavepath, 'http://0.0.0.0:5000/pdf2wav',username, password, token)

    clientObj.pdf2wavConverter()


cli.add_command(generateWavFromPdf)
cli.add_command(generateToken)

if __name__ == "__main__":
    cli()