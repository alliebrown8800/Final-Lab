#!/usr/bin/python3

# Importing libraries:
import RPi.GPIO as GPIO
import time
import json
from clock import Clock
from led8x8 import led8x8

# Pin Setup
dataPin, latchPin, clockPin = 17, 27, 22
digitPins = [6, 5, 13, 19]
motionPin = 4
buzzerPin = 21
switchPin = 18
DHTPin = 23
pwmPin = 16
motorPin = 12
data = 24
latch = 25
clock = 26
shotCheck = True
GPIO.setmode(GPIO.BCM)
GPIO.setup(motionPin, GPIO.IN)
GPIO.setup(buzzerPin, GPIO.OUT)
GPIO.setup(pwmPin, GPIO.OUT)
GPIO.setup(motorPin, GPIO.OUT)
GPIO.setup(data, GPIO.OUT)
GPIO.setup(latch, GPIO.OUT)
GPIO.setup(clock, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50)
pwm.start(0)

chosen_alarm = ''
GPIO.output(buzzerPin,0)

ourClock = Clock(dataPin, latchPin, clockPin, digitPins, switchPin, DHTPin)
matrix = led8x8(data,latch,clock)

pattern = [0b00000000, 0b00000000, 0b00010000, 0b00000000,
           0b00000000, 0b00000000, 0b00000000, 0b00000000]
matrix.updatePattern(pattern)


def cannon(pwm,motorPin):
  pwm.ChangeDutyCycle(2)
  GPIO.output(motorPin,1)
  time.sleep(5)
  pwm.ChangeDutyCycle(6)
  time.sleep(.5)
  GPIO.output(motorPin,0)
  pwm.ChangeDutyCycle(2)
  time.sleep(.5)


try:
  while True:
    with open("alarm.txt", 'r') as f:
      parents_options = json.load(f) # retrieving json data from txt
    chosen_message = str(parents_options['message']) # the message that the parents chose

    if str(parents_options['alarm']) != chosen_alarm or parents_options['alarm'] != 'null': # if the chosen alarm is different than what it was before
      chosen_alarm = str(parents_options['alarm']) # then change it - this will be a string i believe 0345 yanno
      
    # refresh message

    # Get the time:
    minute = time.localtime().tm_min
    # Because the time comes up wrong:
    hour = time.localtime().tm_hour - 5
    if hour < 1: hour = hour + 24
    # Display non-military time:
    if hour > 12: hour = hour - 12
    # Making the time into a list of numbers:
    currentTime = str(hour) + ':' + str(minute)
    checkTime = str(time.localtime().tm_hour - 5)+':'+str(minute)
    print(chosen_alarm)
    print(checkTime)

    if chosen_alarm == checkTime:
      GPIO.output(buzzerPin,1)        
      time.sleep(4)
      if shotCheck:
        cannon(pwm,motorPin)
        shotCheck = False
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