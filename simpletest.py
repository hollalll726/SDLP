#coding: utf-8

import RPi.GPIO as GPIO
import time
import Tkinter

### Am2302 setting
import Adafruit_DHT
# set sensor
sensor = Adafruit_DHT.DHT22
# get pin number
pin = '23'


GPIO.setmode(GPIO.BOARD)

LED = 11

GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)
"""
try:
    while True:
        time.sleep(1)
        # get humidity , temperature from sensor
        humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
        print(humidity)
        if humidity > 80 :
            GPIO.output(LED,GPIO.HIGH)
        else:
            GPIO.output(LED,GPIO.LOW)
except KeyboardInterrupt:
    pass
"""

#def for turn on(off) LED
def func():
    humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
    print(humidity)
    if humidity > 80 :
        GPIO.output(LED,GPIO.HIGH)
    else:
        GPIO.output(LED,GPIO.LOW)
def func2():
    GPIO.output(LED,GPIO.LOW)
    
# Tk instance root
root = Tkinter.Tk()

#label for root
label = Tkinter.Label(root,text='press button')

#locate label
label.pack()

#definite buttons on root
button = Tkinter.Button(root,text='LED',command=func)
button2 = Tkinter.Button(root,text='LEDOFF',command=func2)
#loacte button
button.pack()
button2.pack()

#show root
root.mainloop()

GPIO.cleanup()
