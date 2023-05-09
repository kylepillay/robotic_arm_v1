from adafruit_servokit import ServoKit
from DRV8825 import DRV8825

from arm import Arm
from arm_components.shoulder import Shoulder
from arm_components.claw import Claw
from arm_components.elbow import Elbow
from arm_components.wrist import Wrist
from arm_components.twist_wrist import WristTwist
from arm_components.arm_base import ArmBase

kit = ServoKit(channels=16)
motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))


def set_servo_positions():
    # Shoulder
    kit.servo[5].angle = 0
    kit.servo[6].angle = 180
    # Elbow
    kit.servo[10].angle = 180
    # Wrist
    kit.servo[3].angle = 0
    # Twist Wrist
    kit.servo[11].angle = 90
    # Claw
    kit.servo[12].angle = 180


def initialize_arm():
    arm_base = ArmBase(motor1)
    shoulder = Shoulder(kit.servo[5], kit.servo[6])
    elbow = Elbow(kit.servo[10])
    wrist = Wrist(kit.servo[3])
    twist_wrist = WristTwist(kit.servo[11])
    claw = Claw(kit.servo[12])

    return Arm(arm_base, shoulder, elbow, wrist, twist_wrist, claw)
