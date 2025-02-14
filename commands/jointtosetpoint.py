import commands2

from constants import JointConstants
from subsystems.jointsubsystem import JointSubsystem

class JointToSetpoint(commands2.Command):

    def __init__(self, jointsub: JointSubsystem, setpoint: float):
        self.jointsub = jointsub
        self.setpoint = setpoint

    def initialize(self):
        self.jointsub.go_to_setpoint(self.setpoint)

    def execute(self):
        pass

    def end(self, interrupted):
        pass

    def isFinished(self):
        return self.jointsub.is_at_setpoint()
