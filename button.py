#!/usr/bin/env python


import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.OUT)

try:
    while True:
        button_state = GPIO.input(23)
        if button_state == False:
            GPIO.output(24, True)
            print(datetime.now().strftime("%Y:%m:%d-%H:%M:%S a button was pressed..."))
            time.sleep(0.2)
        else:
            GPIO.output(24, False)
except:
    GPIO.cleanup()
