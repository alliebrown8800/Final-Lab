# LEDdisplay class
from shifter import Shifter    # extend by composition

class LEDdisplay():

  'Class for controlling a 7-segment LED display'

  numbers = [ 
    0b10000000, # 0
    0b11000000, # 1
    0b10100000, # 2
    0b10010000, # 3
    0b10001000, # 4
    0b10000100, # 5
    0b10000010, # 6
    0b10000001, # 7
    0b10000000, # 8
    0b00000000] # 9

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def setNumber(self, num):  # display a given number
    self.shifter.shiftByte(LEDdisplay.numbers[num])