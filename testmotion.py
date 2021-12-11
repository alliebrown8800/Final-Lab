import RPi.GPIO as GPIO

pin_MotionSensor = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_MotionSensor, GPIO.IN)

try: # exception handling
  motion = GPIO.input(pin_MotionSensor) 
  if motion == True:
    print('Motion detected')
  elif motion == False:
    print('No motion detected')

# More exception handling:
except KeyboardInterrupt: 
  print('\nExiting')
except Exception as e: # catch all other errors
  print(e)

GPIO.cleanup()