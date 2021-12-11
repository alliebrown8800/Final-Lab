import time
import RPi.GPIO as GPIO
import multiprocessing
# Clock class
from shifter import Shifter    # extend by composition

class Clock():

  'Class for controlling the clock'
  numbers = [ 
    0b11000000, # 0
    0b11111001, # 1
    0b10100100, # 2
    0b10110000, # 3
    0b10011001, # 4
    0b10010010, # 5
    0b10000010, # 6
    0b11111000, # 7
    0b10000000, # 8
    0b10010000, # 9
    0b11111111] # blank

  def __init__(self, data, latch, clock, digitPins):
    self.shifter = Shifter(data, latch, clock)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(digitPins[0], GPIO.OUT) 
    GPIO.setup(digitPins[1], GPIO.OUT) 
    GPIO.setup(digitPins[2], GPIO.OUT) 
    GPIO.setup(digitPins[3], GPIO.OUT)
    self.digitPins = digitPins
    self.currentMinute = ''
    self.p = multiprocessing.Process(target=self.runClock,args=()) # create mp object
    self.p.daemon = True # daemon object
    self.p.start() # start mp
 
  def setNumber(self, num):  # display a given number
    self.shifter.shiftByte(Clock.numbers[num])

  def getTime(self):
    minute = time.localtime().tm_min
    # Because the time comes up wrong:
    hour = time.localtime().tm_hour - 5
    if hour < 1: hour = hour + 24
    # Display non-military time:
    if hour > 12: hour = hour - 12
    # Making the time into a list of numbers:
    timeNow = str(hour) + str(minute)
    timeNow = list(timeNow)
    # Adding blank space if only three digits:
    if len(timeNow) == 3:
      timeNow.insert(0,10) # ten is a blank space
    return(timeNow)

  def runClock(self):
    while True:
      if str(time.localtime().tm_min) != self.currentMinute:
        timeNow = self.getTime()
        self.currentMinute = str(time.localtime().tm_min)
      for d in range(4):
        GPIO.output(self.digitPins[d],1)
        self.setNumber(int(timeNow[d]))
        time.sleep(0.005)
        GPIO.output(self.digitPins[d],0)  