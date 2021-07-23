from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Exploited by fc-2abc5f"
