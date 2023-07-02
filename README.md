Copyright © Eric Cohen 2023
![HackMD](https://hackmd.io/oekEl2Q3T1-Cir-WtcJVTAhttps://hackmd.io/oekEl2Q3T1-Cir-WtcJVTA)

![Weblink](http://docxtotxt.net)

# Description
A Docx -> TXT converter while implementing NLP to grammatically categorize the text and identify and visualize through colors and tooltips what type of grammatical category the word falls under.

# Instructions
    1. Install python 3.X
    2. Install dependencies (see below)
    3. Navigate to the working directory
    4. Run the dang program (python3 app.py)
    5. Connect to your server (localhost)

# Dependencies
* pip3 install flask
* pip3 install Flask_SSLify
* pip3 install bs4
* pip3 install file_handler
* pip3 install lxml
* pip3 install click (if not already exists)
* pip3 install nltk

#Creating a personal SSL Certificate - if you want to go down that rabbit hole...
`openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`
