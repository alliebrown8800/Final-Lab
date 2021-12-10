# LEDdisplay class
from shifter import Shifter    # extend by composition

class LEDdisplay():

  'Class for controlling a 7-segment LED display'

  numbers = [ 
    0b00000011, # 0
    0b11110011, # 1
    0b00100101, # 2
    0b00001101, # 3
    0b10011001, # 4
    0b01001001, # 5
    0b01000001, # 6
    0b00011111, # 7
    0b11111111, # 8
    0b00011000] # 9

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def setNumber(self, num):  # display a given number
    self.shifter.shiftByte(LEDdisplay.numbers[num])