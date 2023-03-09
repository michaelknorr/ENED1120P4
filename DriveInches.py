#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
#Created Objects
left_motor=Motor(Port. A)
right_motor=Motor(Port. B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104) 
gyro=GyroSensor(Port.S4)
In= 84
if In<=12:
    Distance = ((In+1)/11)*300
elif In<=24:
    Distance = ((In+1+In/12 )/11)*300
elif In<=36:
    Distance = ((In+2+In/12 )/11)*300
elif In<=48:
    Distance = ((In+3+In/12 )/11)*300
elif In<=60:
    Distance=((In+4+In/12)/11)*300
elif In<=84:
    Distance=((In+6+In/12)/11)*300

GSPK= 2.5
speed=250



# Actual running program
gyro.reset_angle(0)
if Distance >0:

    while robot.distance() <= Distance:
        correction = (0 - gyro.angle())*GSPK
        robot.drive(speed, correction)
    robot.stop()
    left_motor.brake()
    right_motor.brake() 
else: 
    while robot.distance()<= Distance:
        correction = (0-gyro.angle())*GSPK
        robot.drive(-speed, correction)
    robot.stop()
    left_motor.brake()
    right_motor.brake()

#Turn Function



