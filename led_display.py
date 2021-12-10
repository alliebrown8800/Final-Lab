# LEDdisplay class
from shifter import Shifter    # extend by composition

class LEDdisplay():

  'Class for controlling a 7-segment LED display'
  # zero is ON, 1 is OFF
  numbers = [ 
   #0b12345678 
    0b11000000, # 0
    0b11111001, # 1
    0b10100100, # 2
    0b10110000, # 3
    0b10011001, # 4
    0b10010010, # 5
    0b10000010, # 6
    0b11111000, # 7
    0b10000000, # 8
    0b10010000] # 9

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def setNumber(self, num):  # display a given number
    self.shifter.shiftByte(LEDdisplay.numbers[num])