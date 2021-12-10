import RPi.GPIO as GPIO
from clock import Clock

dataPin, latchPin, clockPin = 17, 27, 22
digitPins = [6, 5, 13, 19]

try: # exception handling
  ourClock = Clock(dataPin, latchPin, clockPin, digitPins)
  ourClock.runClock()

# More exception handling:
except KeyboardInterrupt: 
  print('\nExiting')
except Exception as e: # catch all other errors
  print(e)

GPIO.cleanup()