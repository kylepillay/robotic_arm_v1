import math
from time import sleep


def move(direction, amount, servo):
    angle = math.ceil(servo.angle)
    for n in range(amount):
        if direction == "negative":
            angle -= 1
        else:
            angle += 1

        if math.ceil(servo.angle) >= 0:
            servo.angle = angle
            sleep(0.02)
        else:
            print("maximum")
            break


def move_to_point(servo, point, move_backward, move_forward):
    angle = math.ceil(servo.angle)
    if (point - angle) > 0:
        move_backward(point - angle)
    else:
        move_forward(abs(point - angle))
