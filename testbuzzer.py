import time
from gpiozero import Buzzer

buzzer = Buzzer(21)

chosen_alarm = '1050'

while True:
  # Get the time:
  minute = time.localtime().tm_min
  # Because the time comes up wrong:
  hour = time.localtime().tm_hour - 5
  if hour < 1: hour = hour + 24
  # Display non-military time:
  if hour > 12: hour = hour - 12
  # Making the time into a list of numbers:
  timeNow = str(hour) + str(minute)

  if chosen_alarm == timeNow:
    buzzer.on()
    time.sleep(5)
    buzzer.off(5)
    time.sleep(5)