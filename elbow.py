import math
from time import sleep

class Elbow:
    def __init__(self, servo):
        self.servo = servo
    
    def moveForward(self, amount):
        angle = math.ceil(self.servo.angle)
        for n in range(amount):
            angle -= 1
            if math.ceil(self.servo.angle) >= 0:
                self.servo.angle = angle
                sleep(0.02)
            else:
                print("maximum")
                break;
    
    def moveBackward(self, amount):
        angle = math.ceil(self.servo.angle)
        for n in range(amount):
            angle += 1
            if math.floor(self.servo.angle) <= 180:
                self.servo.angle = angle
                sleep(0.02)
            else:
                print("maximum")
                break;
