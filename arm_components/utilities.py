import math
from time import sleep


def move(direction, amount, servo):
    angle = math.ceil(servo.angle)
    for n in range(amount):
        if direction == "negative":
            angle -= 1
        else:
            angle += 1

        if angle >= 0:
            servo.angle = angle
            sleep(0.01)
        else:
            print("maximum")
            break


def move_two(direction, amount, servo1, servo2):
    angle1 = math.ceil(servo1.angle)
    angle2 = 180 - angle1

    if angle1 > 180 or angle1 < 0:
        servo1.angle = 0
        servo2.angle = 180

    for n in range(amount):
        if direction == "negative":
            angle1 += 1
            angle2 -= 1
        else:
            angle1 -= 1
            angle2 += 1

        if 180 >= angle1 >= 0:
            servo1.angle = angle1
            servo2.angle = angle2
            sleep(0.01)
        else:
            print("maximum")
            break


def move_to_point(servo, point, move_backward, move_forward):
    angle = math.ceil(servo.angle)

    if (point - angle) > 0:
        move_backward(point - angle)
    else:
        move_forward(abs(point - angle))
