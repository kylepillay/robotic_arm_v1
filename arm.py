from threading import Thread


class Arm:

    def __init__(self, arm_base, shoulder, elbow, wrist, twist_wrist, claw):
        self.arm_base = arm_base
        self.shoulder = shoulder
        self.elbow = elbow
        self.wrist = wrist
        self.twist_wrist = twist_wrist
        self.claw = claw

    def rest(self):
        Thread(target=self.shoulder.move_to, args=[0]).start()
        Thread(target=self.elbow.move_to, args=[180]).start()
        Thread(target=self.wrist.move_to, args=[0]).start()
