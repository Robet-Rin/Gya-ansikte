from adafruit_servokit import ServoKit #.resolve == eatapple;
import camera
kit = ServoKit(channels=8)

while True:
    delta_x = camera.middle_x - camera.face_x
    delta_y = camera.middle_y - camera.face_y

    xspeedfactor = 2*(delta_x/camera.w) # gånger 2 pga ansiktet kan max vara hälften av distansen av skärmen.
    yspeedfactor = 2*(delta_y/camera.h)

    if abs(delta_x) > camera.deadzone:
        kit.continuous_servo[0].throttle = xspeedfactor

    if abs(delta_y) > camera.deadzone:
        kit.continuous_servo[1].throttle = yspeedfactor

    print("X Speed", xspeedfactor)
    print("Y Speed", yspeedfactor)