import RPi.GPIO as GPIO
import time

pin_MotionSensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_MotionSensor, GPIO.IN)

try: # exception handling
  while True:
    motion = GPIO.input(pin_MotionSensor) 
    if motion == True:
      print('Motion detected')
    elif motion == False:
      print('No motion detected')
    time.sleep(.1)

# More exception handling:
except KeyboardInterrupt: 
  print('\nExiting')
except Exception as e: # catch all other errors
  print(e)

GPIO.cleanup()