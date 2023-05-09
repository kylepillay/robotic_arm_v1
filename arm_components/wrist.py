from arm_components.arm_component_base import ArmComponentBase
from arm_components import utilities


class Wrist(ArmComponentBase):
    def __init__(self, servo):
        super().__init__(servo, "negative" , "positive")

