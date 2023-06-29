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
    if request.method == 'POST':
        print("Post request")
        f=request.files['file-txt']
        print("saving...")
        f.save(f.filename)
        print("saved.")
        c = converter().run(f.filename)  # Get the path of the converted text file
        print("Working...")
        lines = []  # Initialize lines
        with open(c, 'r') as file:  # Open the converted text file
            lines = [line.rstrip() for line in file if line.strip()]  # Read lines from the converted text file. Strips new line char
        converter().delFile(c)  # Delete the converted text file
        converter().delFile(f.filename) # Deleted the original doc(x) file.
        response = render_template('./uploaded.html', file=lines)
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337, debug=True)
