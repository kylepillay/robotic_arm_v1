import utilities


class ArmComponentBase:
    def __init__(self, servo):
        self.servo = servo

    def move_forward(self, amount):
        utilities.move("negative", amount, self.servo)

    def move_backward(self, amount):
        utilities.move("positive", amount, self.servo)

    def move_to(self, point):
        utilities.move_to_point(self.servo, point, self.move_backward, self.move_forward)