import RPi.GPIO as GPIO
import time
from led_display import LEDdisplay

# Simple demonstration of the LEDdisplay class.
# Note that we don't need RPi.GPIO here since all the I/O
# is done through the LEDdisplay class (we do however need
# to define the GPIO pins, since LEDdisplay is
# pin-agnostic).

dataPin, latchPin, clockPin = 17, 27, 22
digitPins = [5, 6, 13, 19]
GPIO.setmode(GPIO.BCM)
GPIO.setup(digitPins[0], GPIO.OUT) 
GPIO.setup(digitPins[1], GPIO.OUT) 
GPIO.setup(digitPins[2], GPIO.OUT) 
GPIO.setup(digitPins[3], GPIO.OUT) 

clockDisplay = LEDdisplay(dataPin, latchPin, clockPin)

while True:
  for n in range(4):
    GPIO.output(digitPins[n],1)
    clockDisplay.setNumber(2)
    time.sleep(0.4)
    GPIO.output(digitPins[n],0)
