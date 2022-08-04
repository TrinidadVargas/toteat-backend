from datetime import datetime
from flask import Flask, render_template
from .. import app

@app.route("/")
def home():
    return "Hello World"
