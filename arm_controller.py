from adafruit_servokit import ServoKit

from arm_components.shoulder import Shoulder
from arm_components.claw import Claw
from arm_components.elbow import Elbow
from arm_components.wrist import Wrist
from arm_components.twist_wrist import WristTwist

kit = ServoKit(channels=16)

# Shoulder
kit.servo[5].angle = 100
kit.servo[6].angle = 80

# Elbow
kit.servo[10].angle = 80

# Wrist
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

# This is just for testing
while True:
    try:
        command = input("Enter a command: ").strip()
        if command == "grab":
            claw.grab()
        elif command == "release":
            claw.release()
        elif command == "fs":
            shoulder.move_forward(10)
        elif command == "bs":
            shoulder.move_backward(10)
        elif command == "fe":
            elbow.move_forward(30)
        elif command == "be":
            elbow.move_backward(30)
        elif command == "fw":
            wrist.move_forward(30)
        elif command == "bw":
            wrist.move_backward(30)
        elif command == "twc":
            twist_wrist.twist_wrist_clockwise(30)
        elif command == "twcc":
            twist_wrist.twist_wrist_counter_clockwise(30)
        else:
            print("Sorry, I do not understand the command.")
    except ValueError:
        print("It seems something has gone wrong.")
    

