import RPi.GPIO as GPIO

switchPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(switchPin, GPIO.IN)

while True:
  switch = GPIO.input(switchPin)
  if switch == True:
    print('switch is on')
  elif switch == False:
    print('switch is off')