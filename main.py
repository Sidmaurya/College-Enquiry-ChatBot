
from flask import Flask, render_template, request, Session, session

import aiml

import random
import re

import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

botName = "E-bot"

@app.route("/")
def home():
    global botName
    session['sid'] = random.randint(1,10000) #uuid.uuid4()
    k.learn("std-startup.xml")
    k.respond("load aiml b", session.get('sid'))
    

    return render_template("index.html")

@app.route("/get")
@app.route("/")
def get_bot_response():
    userText = request.args.get('msg')
    return (start(userText))

	




k = aiml.Kernel()

GREETING = ["hii my name is E-Bot(writen in C'vani)) I was created for college enquiry '"]

DEFAULT_RESPONSES = ["I did not get you! Pardon please!","I couldn't understand what you just said! Kindly rephrase"
                     " what you said :-)", "What you are saying is out of my understanding! You can ask me"
                     " queries regrading RCOEM, your attendance and grades" ]

EMPTY_RESPONSES = ["Say something! I would love to help you!","Don't hesitate. I'll answer your queries to the best"
                   " of my knowledge!","Say my friend!"]







def preprocess(inp):
    if(inp!=""):
        if inp[-1]=='.':
            inp = inp[:-1]
    # to remove . symbol between alphabets. Eg. E.G.C becomes EGC
    inp = re.sub('(?<=\\W)(?<=\\w)\\.(?=\\w)(?=\\W)','',inp) 
    # to remove - symbol between alphabet. Eg. E-G-C becomes EGC
    inp = re.sub('(?<=\\w)-(?=\\w)',' ',inp) 
    # to remove . symbol at word boundaries. Eg. .E.G.C. becomes E.G.C
    inp = re.sub('((?<=\\w)\\.(?=\\B))|((?<=\\B)\\.(?=\\w))','',inp)
    # to remove ' ' symbol in acronyms. Eg. E B C becomes EBC
    inp = re.sub('(?<=\\b\\w) (?=\\w\\b)','',inp)
    inp = inp.upper()
#    print(inp)
    return inp



def start(inp):
    print(session.get('sid'))
    # tasks: remove punctuation from input or make it get parsed, do something when no match is found; removed last period to end sentence
    p_inp = preprocess(inp)
    # function for transfer to authentication module
    auth = -1
    
    
    inp = p_inp
    response = k.respond(inp, session.get('sid'))
    if(response=='No match'):
       
            return(response)
    elif(response==""):
        return(random.choice(EMPTY_RESPONSES))
    else: 
        response = re.sub('( )?(http:[%\-_/a-zA-z0-9\\.]*)','<a href="\\2">\\2</a>',response)
        return (response)
    
        





if __name__ == "__main__":
    app.run()
    