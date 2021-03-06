# To get this app working:
# pip3 install .
# source venv/bin/activate
# export FLASK_APP=flaskcorsbypass.py
# python3 -m venv venv
# flask run --reload

# if dependencies aren't found, the app may not be running from venv, can verify from the print(sys.path)

from flask import Flask, request
from flask_cors import CORS
import sys
import json
import requests

app = Flask(__name__)
CORS(app)

@app.route('/relay', methods = ['POST', 'GET'])
def relay():
    data = request.get_json(force=True)
    url = data["url"]
    headers = data["headers"]

    data = requests.get(url=url, headers=headers)

    return data.json()

print(sys.path)

@app.route('/debug', methods = ['POST', 'GET'])
def debug():
    info = ""
    info += "Url params " + str(request.args) + "<br>"

    info += "JSON: " + str(request.get_json(force=True)) + "<br>"
    info += "Data: " + str(request.get_data) + "<br>"

    return info


@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])
def index():
    return "Text is returned"