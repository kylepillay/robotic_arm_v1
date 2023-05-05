import utilities


class Elbow:
    def __init__(self, servo):
        self.servo = servo

    def move_forward(self, amount):
        utilities.move("negative", amount, self.servo)

    def move_backward(self, amount):
        utilities.move("negative", amount, self.servo)