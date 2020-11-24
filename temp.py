import time
import pycom
from pysense import Pysense
from Adafruit_IO import Client, Feed

from SI7006A20 import SI7006A20

def temperature ():
    py = Pysense()
    si = SI7006A20(py)

while True:
temp=si.temperature()
aio.send("{}/feeds/temperature".format(username), str(temperature), 21)
currentTemperature = aio.receive("temperature").value print (currentTemperature) print("done")
time.sleep(30)

Data aio = Client("aio_QmnV52FufJZn0MZLS230LGhI2XJE")
