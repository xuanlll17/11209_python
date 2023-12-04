from flask import Flask, render_template,url_for
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")