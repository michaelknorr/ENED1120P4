from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, follow_for_ms, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor
from ev3dev2.sensor import INPUT_2
import time

Location=int(input(("Input the location value of the box: ")))
x=Location-6
Din=(5.0625+6*(x-1))
negDin=(102-6)-(Din)


tank=MoveTank(OUTPUT_B, OUTPUT_A)
tank.gyro=GyroSensor(INPUT_2)
tank.gyro.calibrate()
tank.gyro.reset()

tank.follow_gyro_angle( 
    kp=11,
    ki=0.05,
    kd=3.,
    speed=SpeedPercent(10),
    target_angle=0,
    sleep_time=0.01,
    follow_for=follow_for_ms,
    ms=3400*4.7,
)

tank.turn_left(speed=10, degrees=90, brake=True, error_margin=2, sleep_time=0.01)

time.sleep(2)

tank.gyro.calibrate()
tank.gyro.reset()

tank.follow_gyro_angle(
 kp=-1,
 ki=0.05, 
 kd=0.,
 speed=SpeedPercent(10), 
 target_angle=0,
 sleep_time=0.01, 
 follow_for=follow_for_ms, 
 ms=(10/(16+25/32)*1000*Din)+6460
)

time.sleep(5)

tank.gyro.calibrate()
tank.gyro.reset()

tank.follow_gyro_angle(
kp=-1,
ki=0.05, 
kd=0.,
speed=SpeedPercent(10), 
target_angle=0,
sleep_time=0.01, 
follow_for=follow_for_ms, 
ms=(6460+ (10/(16+25/32)*1000*(96-Din))  
))

tank.turn_left(speed=10, degrees=90, brake=True, error_margin=2, sleep_time=0.01)

time.sleep(2)

tank.follow_gyro_angle( 
    kp=11,
    ki=0.05,
    kd=3.,
    speed=SpeedPercent(10),
    target_angle=0,
    sleep_time=0.01,
    follow_for=follow_for_ms,
    ms=3400*4.7,
)
