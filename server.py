from flask import Flask

app = Flask(__name__)

# Config
PORT = 9999
host = "0.0.0.0"

@app.route("/")
def home():
    return "<p>Hello<p>"

app.run(host=host,port=PORT)