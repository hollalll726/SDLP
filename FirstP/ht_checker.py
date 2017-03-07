#coding:utf-8

import RPi.GPIO as GPIO
import time

###Am2302 setting
import Adafruit_DHT
#set sensor
sensor = Adafruit_DHT.DHT22
#get pin number
pin '23'

GPIO.setmode(GPIO.BOARD)

LED = 11 
