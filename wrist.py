import math
from time import sleep

class Wrist:
    def __init__(self, servo):
        self.servo = servo
    
    def moveForward(self, amount):
        angle = math.ceil(self.servo.angle)
        for n in range(amount):
            angle += 1
            self.servo.angle = angle
            sleep(0.02)
    
    def moveBackward(self, amount):
        angle = math.ceil(self.servo.angle)
        for n in range(amount):
            angle -= 1
            self.servo.angle = angle
            sleep(0.02)