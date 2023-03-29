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

kit.servo[0].angle = 150
kit.servo[1].angle = 150

kit.servo[2].angle = 150
kit.servo[3].angle = 150

kit.servo[4].angle = 170

kit.servo[5].angle = 70

kit.servo[6].angle = 0

kit.servo[7].angle = 90

shoulder = Shoulder(kit.servo[0], kit.servo[1])
elbow = Elbow(kit.servo[2], kit.servo[3])
wrist = Wrist(kit.servo[4])
twist_wrist = WristTwist(kit.servo[5])
claw = Claw(kit.servo[6])
arm_base = ArmBase(kit.servo[7])

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
        elif command == "tac":
            arm_base.turnClockwise(30)
        elif command == "tacc":
            arm_base.turnCounterClockwise(30)
        else:
            print("Sorry, I do not understand the command.")
    except ValueError:
        print ("Sorry, I do not understand the command.") 
    

