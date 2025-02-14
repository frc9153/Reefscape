import commands2

from constants import LiftConstants, JointConstants, GrabberConstants
from subsystems.liftsubsytem import LiftSubsystem

class LiftToSetpoint(commands2.Command):

    def __init__(self, liftsub: LiftSubsystem, setpoint: float):
        self.liftsub = liftsub
        self.setpoint = setpoint

    def initialize(self):
        self.liftsub.go_to_setpoint(self.setpoint)

    def execute(self):
        pass

    def end(self, interrupted):
        pass

    def isFinished(self):
        return self.liftsub.is_at_setpoint()
