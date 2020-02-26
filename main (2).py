#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import AnalogSensor, UARTDevice

import utime, serial, string, math 
#import IPython.display, imutils
#from matplotlib import pyplot as pyplot

from pybricks.iodevices import AnalogSensor, UARTDevice


# Write your program here
ev3 = EV3Brick()
uart = UARTDevice(Port.S4, 9600, timeout=200)
paddle = Motor(Port.C)
belt = Motor(Port.D)
pusher = Motor(Port.B)
ev3.speaker.beep()
wait(500)
paddle_closed = 0
message = ''
while True:
    belt.dc(23)
    pusher.dc(10)
    try:
       # uart.write('PLEASE WORK'.encode())
       # wait(50)
       if(uart.waiting() > 1):
            message = uart.read(1)
            # print(message)
            # print(type(message))
           # message = message.decode('utf-8') # not too many options on pybricks micropython
            print("The Message is: ", message)
    except:
        # message = uart.read()
        print("FAILED MESSAGE: ", message)
        print(type(message))
    
    if(message == b'2' and paddle_closed == 0):
        paddle.run_angle(100, 90, stop_type = Stop.HOLD, wait = False)
        belt.run_time(100, 2500)
        paddle.run_angle(100, -90, stop_type = Stop.HOLD, wait = False)
        paddle_closed = 1

    if(message == b'0' and paddle_closed == 1):
        paddle_closed = 0


'''
SETUP OF SENSORS AND MOTORS
'''



#camera = UARTDevice(Port.S4, 9600, timeout = 2000) # two seconds

'''
DEFINING FUNCTIONS
'''
def get_Image_test():
    camera.write("Hello RPI".encode())
    message = camera.read(camera.waiting())
    print(message.decode())

def detect_Color(imgfile):
    print("DONE")





'''
MAIN LOOP
'''

#     get_Image_test()
   