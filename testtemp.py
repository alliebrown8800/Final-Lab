import Adafruit_DHT
import time

while True:
  temperature = Adafruit_DHT.read_retry(23)
  print(temperature)
  time.sleep(.2)