import math
from time import sleep

class ArmBase:
    def __init__(self, servo):
        self.servo = servo
    
    def turnClockwise(self, amount):
        angle = math.ceil(self.servo.angle)
        for n in range(amount):
            angle -= 1
            self.servo.angle = angle
            sleep(0.02)
    
    def turnCounterClockwise(self, amount):
        angle = math.ceil(self.servo.angle)
        for n in range(amount):
            angle += 1
            self.servo.angle = angle
            sleep(0.02)

