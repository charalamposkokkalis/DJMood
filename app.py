from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'GTXS VALE TO ARISTERO LAY'   