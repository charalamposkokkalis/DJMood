from flask import Flask, render_template, request
from wtforms import Form, StringField, validators


# local imports
# from chatbot import talk_to_user
from mood_extraction import sentiment_analysis

# Model
class InputForm(Form):
    r = StringField(u'The text: ', [validators.length(max=1000)])

# text = " ".join(talk_to_user()[0:3])
# results = sentiment_analysis(text)
# print(results)

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        r = sentiment_analysis(form.r.data)

        return render_template("first.html", form=form, s=r)
    else:
        return render_template("second.html", form=form) 
    
app.run(host='0.0.0.0',port=81)

