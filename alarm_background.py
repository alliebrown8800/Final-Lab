#!/usr/bin/python3

# This code runs continually in the background

# We need to do a few things here:
# Retrieve alarm time and message from html
# Read temperature
# Have buzzer go off - automatically change display to time
#   Monitor movement
#   Shoot cannon at 1 minute or so

# Separately:
# Change display if button is pressed

# Importing libraries:
import RPi.GPIO as GPIO
import time
import json

# Naming pins
pin1 = 19
pin2 = 16
pin3 = 20
dataPin, latchPin, clockPin = 17, 27, 22
digitPins = [6, 5, 13, 19]

# Setting pins as inputs or outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)

chosen_alarm = ''

while True:
  with open("alarm.txt", 'r') as f:
    parents_options = json.load(f) # retrieving json data from txt
  chosen_message = str(parents_options['message']) # the message that the parents chose
  print(chosen_message)

  if str(parents_options['alarm']) != chosen_alarm: # if the chosen alarm is different than what it was before
    chosen_alarm = str(parents_options['alarm']) # then change it - this will be a string i believe 0345 yanno
    print(chosen_alarm)

  time.sleep(5)