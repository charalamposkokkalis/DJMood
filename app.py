from flask import Flask, render_template
from chatbot import talk_to_user
from mood_extraction import sentiment_analysis

text = " ".join(talk_to_user()[0:3])
textvar = 'Text: ' + text + ' Score: ' + str(sentiment_analysis(text)[0])

app = Flask(__name__)

@app.route('/')
def home():  
    return render_template('home.html',var=textvar)
    
app.run(host='0.0.0.0', port= 81)