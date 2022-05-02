
import serial 
from time import sleep
while True:
    ser = serial.Serial ("/dev/ttyUSB0", 9600)
    received_data = ser.read()
    sleep(0.08)
    data_left = ser.inWaiting()             
    received_data += ser.read(data_left)
    a = received_data.decode('utf-8')
    print(a) 
