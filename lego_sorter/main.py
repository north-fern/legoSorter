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
import IPython.display, imutils
from matplotlib import pyplot as pyplot

'''
SETUP OF SENSORS AND MOTORS
'''
ev3 = EV3Brick()
#paddle = Motor(Port.S1)
#belt1 = Motor(Port.S2)
camera = UARTDevice(Port.S4, 9600, timeout = 2000) # two seconds

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

ev3.speaker.beep()

while True:
    get_Image_test()