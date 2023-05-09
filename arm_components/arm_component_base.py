from arm_components import utilities


class ArmComponentBase:
    def __init__(self, servo, forward, backward):
        self.servo = servo
        self.forward = forward
        self.backward = backward

    def move_forward(self, amount):
        utilities.move(self.forward, amount, self.servo)

    def move_backward(self, amount):
        utilities.move(self.backward, amount, self.servo)

    def move_to(self, point):
        utilities.move_to_point(self.servo, point, self.move_backward, self.move_forward)