# Final Lab
# Allison Brown and Daniel Susson

import time

minute = time.localtime().tm_min
# Because the time comes up wrong:
hour = time.localtime().tm_hour - 5
if hour < 1: hour = hour + 24
# Display non-military time:
if hour > 12: hour = hour - 12
# Making the time into a list of numbers:
timeNow = str(hour) + ':' + str(minute)
print(timeNow)
print(type(timeNow))


  if chosen_alarm == timeNow:
    buzzer.on()
    time.sleep(5)
    while GPIO.input(motionPin) == False:
      buzzer.on()
      time.sleep(.5)
      buzzer.off()
      time.sleep(.5)
    buzzer.off()