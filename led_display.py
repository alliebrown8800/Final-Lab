# LEDdisplay class
from shifter import Shifter    # extend by composition

class LEDdisplay():

  'Class for controlling a 7-segment LED display'

  numbers = [ 
    0b10000001, # 0
    0b01000001, # 1
    0b00100001, # 2
    0b00010001, # 3
    0b00001001, # 4
    0b00000101, # 5
    0b00000011, # 6
    0b00000001, # 7
    0b00000001, # 8
    0b00000001] # 9

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def setNumber(self, num):  # display a given number
    self.shifter.shiftByte(LEDdisplay.numbers[num])