import utilities


class WristTwist:
    def __init__(self, servo):
        self.servo = servo

    def twist_wrist_clockwise(self, amount):
        utilities.move("negative", amount, self.servo)

    def twist_wrist_counter_clockwise(self, amount):
        utilities.move("positive", amount, self.servo)
