#!/usr/bin/python
#-*- coding:utf-8 -*-
""" Lambda Response Function """

import json

from flask import Flask
from flask import request
from flask import make_response

from LED_ONOFF import *

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN ="1d9d3c1df94d423d8d6fe586fe6e3d0c"

app = Flask(__name__)

@app.route('/message', methods=["POST"])
def message():
    request_data = request.get_json(silent=True)
    print(request_data)
    apiai_client = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    text_request = apiai_client.text_request()
    text_request.lang = 'ko'  # optional, default value equal 'en'
    text_request.session_id = request_data['user_key']
    text_request.query = request_data['content']
    data = text_request.getresponse()
    response_data = data.read().decode('utf8')
    response_data = json.lads(response_data)
    
    a = LEDONOFF()

    print(response_data)
    res = json.dumps({'message': {'text': response_data['result']['fulfillment']['speech']}},
                     indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

@app.route('/keyboard', methods=['GET'])
def keyboard():
    res = json.dumps({'type': 'text'}, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


