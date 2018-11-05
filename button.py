#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from datetime import datetime

class Button:

    red_button = 23
    blue_button = 25
    led = 24

    def setup(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.red_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.led, GPIO.OUT)
        GPIO.setup(self.blue_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print ("Setup complete")

    def run(self):
        print ("Running...")
        
        red_pressed = False
        blue_pressed = True

        try:
            while True:
                red_button_state = GPIO.input(self.red_button)
                blue_button_state = GPIO.input(self.blue_button)
                if red_button_state == False and red_pressed == False:
                    self.flickLED(red_pressed)
                    red_pressed = True
                    print(datetime.now().strftime("%Y:%m:%d-%H:%M:%S RED was pressed"))
                if red_button_state == True:
                    red_pressed = False
                if blue_button_state == False and blue_pressed == False:
                    self.flickLED(blue_pressed)
                    blue_pressed = True
                    print(datetime.now().strftime("%Y:%m:%d-%H:%M:%S BLUE was pressed"))
                if blue_button_state == True:
                    blue_pressed = False
        except:
            print ("Error, closing")
            GPIO.cleanup()


    def flickLED(self, pressed):
        if (pressed):
            pass
        else:
            GPIO.output(self.led, True)
            time.sleep(.2)
            GPIO.output(self.led, False)


button = Button()
button.setup()
button.run()
