import RPi.GPIO as GPIO
import time

switchPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(switchPin, GPIO.IN)


try: # exception handling
  while True:
    switch = GPIO.input(switchPin)
    if switch == True:
      print('switch is on')
    elif switch == False:
      print('switch is off')
    time.sleep(1)

# More exception handling:
except KeyboardInterrupt: 
  print('\nExiting')
except Exception as e: # catch all other errors
  print(e)

GPIO.cleanup()
