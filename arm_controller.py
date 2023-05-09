from initialize import set_servo_positions, initialize_arm


set_servo_positions()
arm = initialize_arm()

# This is just for testing
while True:
    command = input("Enter a command: ").strip()
    if command == "grab":
        arm.claw.grab()
    elif command == "release":
        arm.claw.release()
    elif command == "fs":
        arm.shoulder.move_forward(10)
    elif command == "bs":
        arm.shoulder.move_backward(10)
    elif command == "mts":
        arm.shoulder.move_to(0)
    elif command == "fe":
        arm.elbow.move_forward(30)
    elif command == "be":
        arm.elbow.move_backward(30)
    elif command == "mte":
        arm.elbow.move_to(90)
    elif command == "fw":
        arm.wrist.move_forward(30)
    elif command == "bw":
        arm.wrist.move_backward(30)
    elif command == "twc":
        arm.twist_wrist.move_forward(30)
    elif command == "twcc":
        arm.twist_wrist.move_backward(30)
    elif command == "tc":
        arm.arm_base.turn_clockwise(30)
    elif command == "tcc":
        arm.arm_base.turn_counter_clockwise(30)
    else:
        print("Sorry, I do not understand the command.")
