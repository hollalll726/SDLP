#!/usr/bin/python
#-*- coding:utf-8 -*-
""" Lambda Response Function """

import json

from flask import Flask
from flask import request
from flask import make_response


try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

import RPi.GPIO as GPIO
import Adafruit_DHT
class LEDONOFF:
    #LED setting
    GPIO.setmode(GPIO.BOARD)
    LED = 11
    #am2302 setting
    pin = '23'
    sensor = Adafruit_DHT.DHT22

    GPIO.setup(LED,GPIO.OUT,initial = GPIO.LOW)
    
    def LED_ON(self):
        GPIO.output(self.LED,GPIO.HIGH)
    def LED_OFF(self):
        GPIO.output(self.LED,GPIO.LOW)
    def GPIO_OFF(self):
        GPIO.cleanup()
    def ht_check(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor,self.pin)
        return humidity,temperature

CLIENT_ACCESS_TOKEN ="1d9d3c1df94d423d8d6fe586fe6e3d0c"

app = Flask(__name__)
yo = LEDONOFF()

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
    response_data = json.loads(response_data)
    answer = "" 
    if 'action' in response_data['result']:
      answer = IOT_handler(response_data['result']['action'])
    if answer is not "":
        res = json.dumps({'message': {'text': answer}},
                    indent=4)
    else:
        res = json.dumps({'message': {'text': response_data['result']['fulfillment']['speech']}},
                       indent=4)
    r = make_response(res)
    print(response_data)
    r.headers['Content-Type'] = 'application/json'
    return r

@app.route('/keyboard', methods=['GET'])
def keyboard():
    res = json.dumps({'type': 'text'}, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def IOT_handler(req):
    if req == "LEDON":
      yo.LED_ON()
      return ""
    elif req == "LEDOFF":
      yo.LED_OFF()
      return ""
    elif req == "ht_checker":
      h,t = yo.ht_check()
      return "현재 온도 :"+str(h)+"\n현재 습도 :"+str(t)

if __name__ == "__main__":
  try:
    app.run(host = '192.168.0.10')
  except KeyboardInterrupt:
    yo.GPIO.OFF()
    print("server-end")
