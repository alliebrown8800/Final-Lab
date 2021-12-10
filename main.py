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