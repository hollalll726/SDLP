#coding: utf-8

import RPi.GPIO as GPIO
import time


class LEDONOFF:
  GPIO.setmode(GPIO.BOARD)
  LED = 11
  GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

  def LED_ON(self):
    GPIO.output(self.LED,GPIO.HIGH)

  def LED_OFF(self):
    GPIO.output(self.LED,GPIO.LOW)

  def GPIO_OFF(self):
    GPIO.cleanup()
    
