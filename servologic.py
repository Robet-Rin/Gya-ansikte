from adafruit_servokit import ServoKit #.resolve == eatapple;
import camera
import time

kit = ServoKit(channels=8)
x, y = kit.continuous_servo[0], kit.continuous_servo[1]

def stop():
    x.throttle = 0 #x-led
    y.throttle = 0 #y-led

def servo_active():
    try:

        while True:
            delta_x = camera.middle_x - camera.face_x
            delta_y = camera.middle_y - camera.face_y

            xspeedfactor = 2*(delta_x/camera.w) # gånger 2 pga ansiktet kan max vara hälften av distansen av skärmen.
            yspeedfactor = 2*(delta_y/camera.h)

            if abs(delta_x) > camera.deadzone:
                x.throttle = max(min(xspeedfactor, -1), 1)
            else:
                x.throttle = 0

            if abs(delta_y) > camera.deadzone:
                y.throttle = max(min(yspeedfactor, -1), 1)
            else:
                y.throttle = 0

            #print("X Speed", xspeedfactor)
            #print("Y Speed", yspeedfactor)
            time.sleep(0.02)
    finally:
        stop()

def servo_passive():
    try:
        while True:
            x.throttle = 0.5
            time.sleep(2.5)
            x.throttle = 0
            time.sleep(1)
            x.throttle = -0.5
            time.sleep(2.5)
            x.throttle = 0
            time.sleep(1)
    finally:
        stop() 