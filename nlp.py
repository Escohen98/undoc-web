#Class used to help with word type identification
#Uses nltk natural language processing (NLP) library

import nltk
import os
nltk.download('averaged_perceptron_tagger')
nltk.data.path.append("/usr/share/nltk_data")
nltk.download('punkt')
os.environ['NLTK_DATA'] = 'path_to_nltk_data' #Environment variable

class natty():

    #Gets the type of text and returns a tuple.
    #Taken from https://stackoverflow.com/questions/32411594/identify-the-word-as-a-noun-verb-or-adjective
    def tokenizeText(self,text):
        text = nltk.word_tokenize(text)
        result = nltk.pos_tag(text)
        return result


    #Creates the text to be passed into html
    #Takes in an array of tuples then returns the span array
    def buildHTML(self,arr):
        spanArr = []
        for word in arr:
            spanArr.append('<span class="' + word[1] + '">'+word[0]+'</span>')
        return spanArr

    #Combines the spans
    #Returns result
    def combineSpans(self,arr):
        line = ""
        for span in arr:
            line += span + " "
        return line.strip()

    #Puts all of 'em together
    def run(self,text):
        result = self.combineSpans(self.buildHTML(self.tokenizeText(text)))
        return result
