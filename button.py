#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from datetime import datetime

class Button:

    def setup():
        GPIO.setmode(GPIO.BCM)

        red_button = 23
        blue_button = 25
        led = 24

        GPIO.setup(red_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(led, GPIO.OUT)
        GPIO.setup(blue_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def run():
        try:
            while True:
                red_button_state = GPIO.input(red_button)
                blue_button_state = GPIO.input(blue_button)
                if red_button_state == False:
                    flickLED()
                    print(datetime.now().strftime("%Y:%m:%d-%H:%M:%S RED was pressed"))
                if blue_button_state == False:
                    flickLED()
                    print(datetime.now().strftime("%Y:%m:%d-%H:%M:%S BLUE was pressed"))
        except:
            GPIO.cleanup()


    def flickLED():
        GPIO.output(led, True)
        time.sleep(0.02)
        GPIO.output(led, False)
