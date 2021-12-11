# Final Lab
# Allison Brown and Daniel Susson

import time
print(time.localtime())
print(time.localtime().tm_hour)
print(time.localtime().tm_min)

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)


     
# Driver code
timeNow = str(time.localtime().tm_hour-5) + str(time.localtime().tm_min)
timeNow = list(timeNow)
print(timeNow)

print(timeNow[0])


for d in range(4):
  print(timeNow[d])
  time.sleep(0.001)

minute = time.localtime().tm_min
# Because the time comes up wrong:
hour = time.localtime().tm_hour - 5
if hour < 1: hour = hour + 24
# Display non-military time:
if hour > 12: hour = hour - 12
# Making the time into a list of numbers:
timeNow = str(hour) + str(minute)
print(type(timeNow))