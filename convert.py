import os
import zipfile
import subprocess
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

#Converts word document to text
#Taken from https://python.plainenglish.io/how-to-read-docx-files-with-python-b2ec17bcb277
class converter():

    def run(self, file):
        filename = file[:file.rfind(".")]
        extension = file[file.rfind(".")+1:]
        #Checks to make sure correct file path. Should never occur theoretically.
        if (not ((extension == "docx" or extension == "doc") and os.path.isfile(file))):
            print("Invalid file. Please choose an existing 'doc' or 'docx' file.")
            handler.invalidfile()
        print("ran")
        return self.docToTxt(filename)


    #Creates zip object from word document
    #Pulls and formats xml
    #Extracts text from XML and parses to text document.
    #Adapted from my previous project
    #https://github.com/escohen98/undoc
    def docToTxt(self, folder):
        #Reading lines. Efficient?
        doc = zipfile.ZipFile(folder + ".docx")
        #Turns 1 line into formatted XML
        prettyXML = BeautifulSoup(doc.read('word/document.xml'), features="xml").prettify()
        root = ET.fromstring(prettyXML)

        namespace = {'w': "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        text = root.findall('.//w:t', namespace) #All text is stored in <w:t*>

        #Used to have an overwrite handler, but doesn't matter now
        #File is getting deleted later anyway.
        g = open(folder + '.txt', 'w')
        for t in text: #XML is one line, but just to be safe..
            g.write(t.text)
        g.close()

        file = folder + ".txt"
        file_exists = os.path.isfile(file)

        if file_exists:
            print("returning...")
            return file
                    #p = subprocess.Popen(["notepad.exe", file])

    #Helper function to delete file.
    def delFile(self, filename):
        os.remove(filename)
