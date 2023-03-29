import math
from time import sleep

class WristTwist:
    def __init__(self, servo):
        self.servo = servo
    
    def twistClockwise(self, amount):
        angle = math.ceil(self.servo.angle)
        for n in range(amount):
            angle -= 1
            self.servo.angle = angle
            sleep(0.02)
    
    def twistCounterClockwise(self, amount):
        angle = math.ceil(self.servo.angle)
        for n in range(amount):
            angle += 1
            self.servo.angle = angle
            sleep(0.02)
