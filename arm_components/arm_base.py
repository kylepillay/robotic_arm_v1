import utilities


class ArmBase:
    def __init__(self, servo):
        self.servo = servo

    def turn_clockwise(self, amount):
        utilities.move("negative", amount, self.servo)

    def turn_counter_clockwise(self, amount):
        utilities.move("positive", amount, self.servo)
