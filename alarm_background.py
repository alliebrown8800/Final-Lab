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
from gpiozero import Buzzer

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

buzzer = Buzzer(21)

chosen_alarm = ''

ourClock = Clock(dataPin, latchPin, clockPin, digitPins)

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
  timeNow = str(hour) + ':' + str(minute)

  if chosen_alarm == timeNow:
    buzzer.on()
