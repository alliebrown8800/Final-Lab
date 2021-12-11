#!/usr/bin/python3

# We need to do a few things here:
# Read temperature
# Have buzzer go off
#   Monitor movement
#   Shoot cannon at 1 minute or so

# Separately:
# Change display if button is pressed

# Importing libraries:
import RPi.GPIO as GPIO
import time
import json
from clock import Clock

# Pin Setup
dataPin, latchPin, clockPin = 17, 27, 22
digitPins = [6, 5, 13, 19]
motionPin = 14
buzzerPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(motionPin, GPIO.IN)
GPIO.setup(buzzerPin, GPIO.OUT)

chosen_alarm = ''
GPIO.output(buzzerPin,0)

ourClock = Clock(dataPin, latchPin, clockPin, digitPins)

try:
  while True:
    with open("alarm.txt", 'r') as f:
      parents_options = json.load(f) # retrieving json data from txt
    chosen_message = str(parents_options['message']) # the message that the parents chose

    if str(parents_options['alarm']) != chosen_alarm or parents_options['alarm'] == 'null': # if the chosen alarm is different than what it was before
      chosen_alarm = str(parents_options['alarm']) # then change it - this will be a string i believe 0345 yanno
      
    # Get the time:
    minute = time.localtime().tm_min
    # Because the time comes up wrong:
    hour = time.localtime().tm_hour - 5
    if hour < 1: hour = hour + 24
    # Display non-military time:
    if hour > 12: hour = hour - 12
    # Making the time into a list of numbers:
    currentTime = str(hour) + ':' + str(minute)
    print(chosen_alarm)
    print(currentTime)


    if chosen_alarm == currentTime:
      GPIO.output(buzzerPin,1)        
      time.sleep(5)
      while GPIO.input(motionPin) == False:
        GPIO.output(buzzerPin,1)
        time.sleep(.5)
        GPIO.output(buzzerPin,0)
        time.sleep(.5)
      GPIO.output(buzzerPin,0)
    
    time.sleep(1)

except KeyboardInterrupt: 
  print('\nExiting')
except Exception as e: # catch all other errors
  print(e)               # delete once code is debugged
  ourClock.p.terminate()      # terminate the process
  ourClock.p.join(2)          # wait up to 2 sec for process termination before ending code

GPIO.cleanup()