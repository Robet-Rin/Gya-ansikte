from adafruit_servokit import ServoKit #.resolve == eatapple;
import camera
kit = ServoKit(channels=8)

def stop():
    kit.continuous_servo[0].throttle = 0
    kit.continuous_servo[1].throttle = 0

def servo_loop():
    try:

        while True:
            delta_x = camera.middle_x - camera.face_x
            delta_y = camera.middle_y - camera.face_y

            xspeedfactor = 2*(delta_x/camera.w) # gånger 2 pga ansiktet kan max vara hälften av distansen av skärmen.
            yspeedfactor = 2*(delta_y/camera.h)

            if abs(delta_x) > camera.deadzone:
                kit.continuous_servo[0].throttle = xspeedfactor
            else:
                kit.continuous_servo[0].throttle = 0

            if abs(delta_y) > camera.deadzone:
                kit.continuous_servo[1].throttle = yspeedfactor
            else:
                kit.continuous_servo[1].throttle = 0

            #print("X Speed", xspeedfactor)
            #print("Y Speed", yspeedfactor)
    finally:
        stop()