from flask import Flask, render_template, request, url_for, redirect
from distutils.log import debug
from fileinput import filename
from convert import converter
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('./home.html')

#New page to handle the file upload / convert.
#Also going to display file on webpage.
@app.route('/uploaded', methods=['POST'])
def uploaded():
    lines = [] #Imagine storing an entire text document in an array
    if request.method == 'POST':
        f=request.files['file-txt']
        save(f.filename)
        c = converter().run(f.filename)
        content = f.read() # Reads the entire content of the file
        f.seek(0)  # Reset file pointer to the beginning
        for line in f:
            line = line.decode("utf-8")  # Decode bytes to string
            lines.append(line)  # Or process the line however you need
        converter().delFile(f.filename)
    return render_template('./uploaded.html', file=lines)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337, debug=True)
