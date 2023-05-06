import math
from time import sleep

import utilities


# When Servo1 is at 0, the arm is full forward

class Shoulder:
    def __init__(self, servo1, servo2):
        self.servo1 = servo1
        self.servo2 = servo2

    def move_forward(self, amount):
        angle1 = math.ceil(self.servo1.angle)
        angle2 = 180 - angle1

        for n in range(amount):
            angle1 -= 1
            angle2 += 1

            if math.floor(self.servo1.angle) >= 0:
                self.servo1.angle = angle1
                self.servo2.angle = angle2
                sleep(0.02)
            else:
                print("maximum")
                break

    def move_backward(self, amount):
        angle1 = math.ceil(self.servo1.angle)
        angle2 = 180 - angle1

        for n in range(amount):
            angle1 += 1
            angle2 -= 1

            if math.floor(self.servo1.angle) <= 180:
                self.servo1.angle = angle1
                self.servo2.angle = angle2
                sleep(0.02)
            else:
                print("maximum")
                break

    def move_to(self, point):
        utilities.move_to_point(self.servo1, point, self.move_backward, self.move_forward)
