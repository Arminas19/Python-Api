from flask import Flask
app = Flask(__name__)

# use flask run to run server
@app.route('/')
def index():
    return 'Hello!'