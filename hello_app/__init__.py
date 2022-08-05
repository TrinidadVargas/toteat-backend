from flask import Flask  # Import the Flask class
from flask_cors import CORS, cross_origin

app = Flask(__name__)    # Create an instance of the class for our use
CORS(app)
