import RPi.GPIO as GPIO
import time
from led_display import LEDdisplay

# Simple demonstration of the LEDdisplay class.
# Note that we don't need RPi.GPIO here since all the I/O
# is done through the LEDdisplay class (we do however need
# to define the GPIO pins, since LEDdisplay is
# pin-agnostic).

dataPin, latchPin, clockPin = 17, 27, 22
digitPins = [6, 5, 13, 19]
GPIO.setmode(GPIO.BCM)
GPIO.setup(digitPins[0], GPIO.OUT) 
GPIO.setup(digitPins[1], GPIO.OUT) 
GPIO.setup(digitPins[2], GPIO.OUT) 
GPIO.setup(digitPins[3], GPIO.OUT) 

clockDisplay = LEDdisplay(dataPin, latchPin, clockPin)
timeNow = str(time.localtime().tm_hour-5) + str(time.localtime().tm_min)
timeNow = list(timeNow)


try: # exception handling
  while True:
    for d in range(4):
      GPIO.output(digitPins[d],1)
      clockDisplay.setNumber(int(timeNow[d])
      time.sleep(0.001)
      GPIO.output(digitPins[d],0)

# More exception handling:
except KeyboardInterrupt: 
  print('\nExiting')
except Exception as e: # catch all other errors
  print(e)

GPIO.cleanup()


