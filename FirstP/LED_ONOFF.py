#coding: utf-8

import RPi.GPIO as GPIO
import time


class LEDONOFF:
  GPIO.setmode(GPIO.BOARD)
  LED = 11
  GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

  def LED_ON():
    GPIO.output(LED,GPIO.HIGH)

  def LED_OFF():
    GPIO.output(LED,LOW)

  def GPIO_OFF():
    GPIO.cleanup()
    
