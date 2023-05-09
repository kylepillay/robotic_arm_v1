from arm_components.arm_component_base import ArmComponentBase


class Wrist(ArmComponentBase):
    def __init__(self, servo):
        super().__init__(servo, "positive", "negative")

