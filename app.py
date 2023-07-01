#Page handler. Upload a docx file, convert to txt
#and highlight based on grammar!!!
#Copyright © Eric Cohen 2023

from flask import Flask, render_template, request, url_for, redirect, send_from_directory
from flask_sslify import SSLify
from distutils.log import debug
from fileinput import filename
from convert import converter
from nlp import natty
import os

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
        print("saving...")
        f.save(filepath)
        print("saved.")
        c = converter().run(filepath)  # Get the path of the converted text file
        lines = []  # Initialize lines
        #Grammar tokenization & highlighting
        with open(c, 'r') as file:  # Open the converted text file
             lines = [natty().run(line.rstrip()) for line in file if line.strip()] # Read lines from the converted text file. Strips new line char
        #converter().delFile(c)  # Delete the converted text file
        #converter().delFile(f.filename) # Deleted the original doc(x) file.
        txt_name = c
        print("txt filename: " + c)
        filename = c.split("\\")[len(c.split("\\"))-1]
        print("docx filename: " + filename)
        docx_name = filename
        response = render_template('./uploaded.html', file=lines, filename=filename, fileName=filename)
    return response

#File download handler
@app.route('/download/<filename>')
def download(filename):
    if filename.__contains__("//"):
        filename = filename.split("//")[len(filename.split("//"))-1]
    elif filename.__contains__("\\"):
        filename.split("\\")[len(filename.split("\\"))-1]
    print(f'Attempting to send: {filename}')
    return send_from_directory(directory='static/downloads/', path=filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337, debug=True)


#---------------------- Celery --------------------#

from celery import Celery
cApp = Celery('tasks', include=['tasks'])

#Monitors activity for file deletion
#Defines activity time and time threshold for user activity
@cApp.task
def monitor_user_activity():
    last_activity_time = get_last_activity_time()
    current_time = get_current_time()
    idle_threshold = 30  # Define the idle threshold in seconds (e.g., 5 minutes)

    if current_time - last_activity_time > idle_threshold:
        path = '../static/downloads/'
        if (docx_name != ""):
            converter().delFile(path + docx_name)  # Implement this function to delete the file
        if (txt_name != ""):
            converter.delFile(path + txt_name)
