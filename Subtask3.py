from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, follow_for_ms, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor, MODE_COL_REFLECT
from ev3dev2.sensor import INPUT_2, INPUT_4
import time

tank=MoveTank(OUTPUT_B, OUTPUT_A)
tank.gyro=GyroSensor(INPUT_2)
tank.gyro.calibrate()
tank.gyro.reset()
tank.color1=ColorSensor(INPUT_4)

tank.follow_gyro_angle(
 kp=-1,
 ki=0.05, 
 kd=0.,
 speed=SpeedPercent(10), 
 target_angle=0,
 sleep_time=0.01, 
 follow_for=follow_for_ms, 
 ms=(10/(16+25/32)*1000*(17+13/16))
)

Barcode=[]
BarcodeType=int(input('Please input the number for barcode type: '))

if tank.color1.reflected_light_intensity < 50:
    Barcode(0)=0
else:
    Barcode(0)=1

tank.follow_gyro_angle(
 kp=-1,
 ki=0.05, 
 kd=0.,
 speed=SpeedPercent(10), 
 target_angle=0,
 sleep_time=0.01, 
 follow_for=follow_for_ms, 
 ms=(10/(16+25/32)*1000*(-0.5))
) 

time.sleep(1.5)

if tank.color1.reflected_light_intensity < 50:
    Barcode(1)=0
else:
    Barcode(1)=1

tank.follow_gyro_angle(
 kp=-1,
 ki=0.05, 
 kd=0.,
 speed=SpeedPercent(10), 
 target_angle=0,
 sleep_time=0.01, 
 follow_for=follow_for_ms, 
 ms=(10/(16+25/32)*1000*(-0.5))
) 

time.sleep(1.5)

if tank.color1.reflected_light_intensity < 50:
    Barcode(2)=0
else:
    Barcode(2)=1

time.sleep(1.5)

tank.follow_gyro_angle(
 kp=-1,
 ki=0.05, 
 kd=0.,
 speed=SpeedPercent(10), 
 target_angle=0,
 sleep_time=0.01, 
 follow_for=follow_for_ms, 
 ms=(10/(16+25/32)*1000*(-0.5))
) 

time.sleep(1.5)

if tank.color1.reflected_light_intensity < 50:
    Barcode(4)=0
else:
    Barcode(4)=1

if Barcode = [0, 1, 1, 1]:
    x=1
    print ('Barcode type 1')
    elif Barcode=[0, 1, 0, 1]:
        print ("barcode type 2")
        x=2
        elif Barcode=[0, 0, 1, 1]:
            print ("barcode type 3")
            x=3
            elif Barcode=[0, 1, 1, 0]:
                print ("barcode type 4")
                x=4
                else:
                    print("barcode error")
                    x=69

time.sleep(1.5)

if x=BarcodeType:
    print ("This barcode is the type requested")
    else:
        print ("This barcode is not the type requested... error!")

