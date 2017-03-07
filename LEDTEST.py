#coding: utf-8

import RPi.GPIO as GPIO
import time
import Tkinter
GPIO.setmode(GPIO.BOARD)

LED = 11

GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)
#def for turn on(off) LED
def func():

    GPIO.output(LED,not GPIO.input(LED))
# Tk instance root
root = Tkinter.Tk()

#label for root
label = Tkinter.Label(root,text='press button')

#locate label
label.pack()

#definite buttons on root
button = Tkinter.Button(root,text='LED',command=func)

#loacte button
button.pack()

#show root
root.mainloop()

GPIO.cleanup()
