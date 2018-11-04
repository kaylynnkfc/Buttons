#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)

red_button = 23
blue_button = 25
led = 24

GPIO.setup(red_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(blue_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        red_button_state = GPIO.input(red_button)
        blue_button_state = GPIO.input(blue_button)
        if red_button_state == False:
            GPIO.output(led, True)
            print(datetime.now().strftime("%Y:%m:%d-%H:%M:%S RED was pressed"))
            time.sleep(0.2)
        if blue_button_state == False:
            GPIO.output(led, True)
            print(datetime.now().strftime("%Y:%m:%d-%H:%M:%S BLUE was pressed"))
            time.sleep(0.2)
        else:
            GPIO.output(led, False)
except:
    GPIO.cleanup()
