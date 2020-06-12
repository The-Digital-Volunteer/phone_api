import json
import sys

from flask import Flask
from flask import request

if len( sys.argv ) < 2:
    print( 'Service URL should be provided' )
    exit( 1 )

GREETING_URL = "https://46elks.com/static/sound/ivr-menu.mp3"
SERVICE_URL = sys.argv[1]

app = Flask(__name__)

@app.route("/incomingCalls", methods=['POST'])
def home():
    print(request.form)
    response = {
        "play": GREETING_URL,
        "next": SERVICE_URL + "/record"
    }
    return json.dumps(response)

@app.route("/record", methods=['POST'])
def record():
    print(request.form)
    response = {
        'record': SERVICE_URL + "/process"
    }
    return json.dumps(response)

@app.route("/process", methods=['POST'])
def process():
    print(request.form)
    return json.dumps({})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5501)
