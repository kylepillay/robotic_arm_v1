

class ArmBase:
    def __init__(self, motor):
        self.motor = motor

    def turn_clockwise(self, amount):
        self.motor.TurnStep(Dir='forward', steps=2048, stepdelay=0.002)
        self.motor.Stop()

    def turn_counter_clockwise(self, amount):
        self.motor.TurnStep(Dir='backward', steps=2048, stepdelay=0.002)
        self.motor.Stop()

