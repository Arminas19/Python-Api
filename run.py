from flask import Flask
app = Flask(__name__)

# use 'flask run' to run server
# video on 31:14 / video link - https://www.youtube.com/watch?v=qbLc5a9jdXo
@app.route('/')
def index():
    return 'Hello!'