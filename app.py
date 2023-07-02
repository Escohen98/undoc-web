#Page handler. Upload a docx file, convert to txt
#and highlight based on grammar!!!
#Copyright © Eric Cohen 2023

from flask import Flask, render_template, request, url_for, redirect, send_from_directory
from flask_sslify import SSLify
from distutils.log import debug
from fileinput import filename
from convert import converter
from nlp import natty
import os, platform

app = Flask(__name__)
sslify = SSLify(app) #Redirects http to https. Apparently doesn't work.
docx_name = ""
txt_name = ""
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('./home.html')

#New page to handle the file upload / convert.
#Also going to display file on webpage.
@app.route('/uploaded', methods=['POST'])
def uploaded():
    if request.method == 'POST':
        print("Post request")
        f=request.files['file-txt']
        filepath = os.path.join('static', 'downloads', f.filename)
        print("original filename: " + f.filename)
        print("saving...")
        f.save(filepath)
        print("saved.")
        c = converter().run(filepath)  # Get the path of the converted text file
        lines = []  # Initialize lines
        #Grammar tokenization & highlighting
        with open(c, 'r') as file:  # Open the converted text file
             lines = [natty().run(line.rstrip()) for line in file if line.strip()] # Read lines from the converted text file. Strips new line char
        file.close()
        #converter().delFile(c)  # Delete the converted text file
        # # Deleted the original doc(x) file.
        if platform.system() == "Windows":
            filename = c.split("\\")[len(c.split("\\"))-1]
        else:
            filename = c.split("/")[len(c.split("/"))-1]
        print("txt filename: " + c)
        txt_name = filename #For celery. May remove later
        print("docx filename: " + f.filename)
        docx_name = f.filename #Also for celery. May also remove later.
        response = render_template('./uploaded.html', file=lines, filename=filename, fileName=filename.split(".txt")[0])
        #filepath = "/static/download/"+f.filename
        converter().delFile(filepath)
    return response

#File download handler
import os

@app.route('/download/<filename>')
def download(filename):
    # Get the full path to the file
    filepath = os.path.join('static', 'downloads', filename)

    if not os.path.isfile(filepath):
        # File does not exist, create a placeholder file
        with open(filepath + '.txt', 'w') as f:
            f.write("I'm sorry, but your file doesn't exist 😢")

        # Return the placeholder file
        return send_from_directory(directory='static/downloads', path=filename, as_attachment=True)

    # File exists, return the actual file
    return send_from_directory(directory='static/downloads', path=filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
