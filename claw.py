import math

class Claw:
    def __init__(self, servo):
        self.servo = servo
    
    def grab(self):
        self.servo.angle = 70
    
    def release(self):
        self.servo.angle = 0