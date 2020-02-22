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

'''
SETUP OF SENSORS AND MOTORS
'''
ev3 = EV3Brick()
paddle = Motor(Port.C)
belt = Motor(Port.D)
#shaker = Motor(Port.B)
#s = serial.Serial('dev/serial0/', 9600)

'''
DEFINING FUNCTIONS
'''
'''
def get_Image_test():
    s.write(b'1')
    array1 = []
    while arrray == []:
       array1 == s.read
       delay(500):
    return array

'''

def detect_Color(array1):
    

    print("done")





'''
MAIN LOOP
'''

ev3.speaker.beep()

while True:
    #get_Image_test()
    belt.dc(40)
    paddle.dc(55)
    

    wait(100)
    paddle.stop()
    wait(1000)
    paddle.dc(-55)
    wait(100)
    paddle.stop()
    wait(1000)
