from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, follow_for_ms, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor
from ev3dev2.sensor import INPUT_2
import time

tank=MoveTank(OUTPUT_B, OUTPUT_A)
tank.gyro=GyroSensor(INPUT_2)
tank.gyro.calibrate()
tank.gyro.reset()

tank.turn_left(speed=10, degrees=180, brake=True, error_margin=2, sleep_time=0.01)

tank.follow_gyro_angle(
 kp=-1,
 ki=0.05, 
 kd=0.,
 speed=SpeedPercent(10), 
 target_angle=0,
 sleep_time=0.01, 
 follow_for=follow_for_ms, 
 ms=(10/(16+25/32)*1000*36)
)

tank.turn_right(speed=10, degrees=90, brake=True, error_margin=2, sleep_time=0.01)

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
 ms=(10/(16+25/32)*1000*96)+6460+6460
)

tank.turn_right(speed=10, degrees=90, brake=True, error_margin=2, sleep_time=0.01)

tank.follow_gyro_angle(
 kp=-1,
 ki=0.05, 
 kd=0.,
 speed=SpeedPercent(10), 
 target_angle=0,
 sleep_time=0.01, 
 follow_for=follow_for_ms, 
 ms=(10/(16+25/32)*1000*36)
)