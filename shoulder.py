import math
from time import sleep

class Shoulder:
    def __init__(self, servo1, servo2):
        self.servo1 = servo1
        self.servo2 = servo2
    
    def moveForward(self, amount):
        angle = math.ceil(self.servo1.angle)
        for n in range(amount):
            angle -= 1
            self.servo1.angle = angle
            self.servo2.angle = angle
            sleep(0.02)
    
    def moveBackward(self, amount):
        angle = math.ceil(self.servo1.angle)
        for n in range(amount):
            angle += 1
            self.servo1.angle = angle
            self.servo2.angle = angle
            sleep(0.02)