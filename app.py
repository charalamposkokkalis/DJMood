# This is the main file, which runs our WebApp
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# local imports
from chatbot import talk_to_user
from mood_extraction import sentiment_analysis
import sprec

# App config.
# DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print (form.errors)
        if request.method == 'POST':
            name=request.form['name']
            password=request.form['password']
            email=request.form['email']
            
            text = name + password + email
            results = sentiment_analysis(text)
            
            emotionVec = []
            emotions = ['Happy', 'Angry', 'Excited', 'Sad', 'Fear', 'Bored']
            for emotion in emotions:
                emotionVec.append(results[emotion])
            print(emotionVec)
            
    
        if form.validate():
        # Save the comment here.
            
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
    
        return render_template('file1.html', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=81)
    
