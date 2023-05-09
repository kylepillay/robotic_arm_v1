import math
from time import sleep

from arm_components import utilities


# When Servo1 is at 0, the arm is full forward

class Shoulder:
    def __init__(self, servo1, servo2):
        self.servo1 = servo1
        self.servo2 = servo2

    def move_forward(self, amount):
        utilities.move_two("positive", amount, self.servo1, self.servo2)

    def move_backward(self, amount):
        utilities.move_two("negative", amount, self.servo1, self.servo2)

    def move_to(self, point):
        utilities.move_to_point(self.servo1, point, self.move_backward, self.move_forward)
