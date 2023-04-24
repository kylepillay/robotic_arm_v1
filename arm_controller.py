from adafruit_servokit import ServoKit
from time import sleep
import math

from shoulder import Shoulder
from claw import Claw
from elbow import Elbow
from wrist import Wrist
from twist_wrist import WristTwist
from arm_base import ArmBase

kit = ServoKit(channels=16)

# Shoulder
kit.servo[5].angle = 100
kit.servo[6].angle = 80

# Elbow
kit.servo[10].angle = 80

#Wrist
kit.servo[3].angle = 180

# Wrist Twist
kit.servo[11].angle = 90

# Claw
kit.servo[12].angle = 180

shoulder = Shoulder(kit.servo[5], kit.servo[6])
elbow = Elbow(kit.servo[10])
wrist = Wrist(kit.servo[3])
twist_wrist = WristTwist(kit.servo[11])
claw = Claw(kit.servo[12])

while True:
    try:
        command = input("Enter a command: ").strip()
        if command == "grab":
            claw.grab()
        elif command == "release":
            claw.release()
        elif command == "fs":
            shoulder.moveForward(10)
        elif command == "bs":
            shoulder.moveBackward(10)
        elif command == "fe":
            elbow.moveForward(30)
        elif command == "be":
            elbow.moveBackward(30)
        elif command == "fw":
            wrist.moveForward(30)
        elif command == "bw":
            wrist.moveBackward(30)
        elif command == "twc":
            twist_wrist.twistClockwise(30)
        elif command == "twcc":
            twist_wrist.twistCounterClockwise(30)
        else:
            print("Sorry, I do not understand the command.")
    except ValueError:
        print ("Sorry, I do not understand the command.") 
    

