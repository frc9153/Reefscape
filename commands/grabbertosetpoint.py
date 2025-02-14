import commands2

from constants import GrabberConstants
from subsystems.grabbersubsystem import GrabberSubsystem

class GrabberToSetpoint(commands2.Command):

    def __init__(self, grabbersub: GrabberSubsystem, setpoint: float, instant: bool):
        self.grabbersub = grabbersub
        self.setpoint = setpoint
        self.instant = instant

    def initialize(self):
        self.grabbersub.go_to_setpoint(self.setpoint)

    def execute(self):
        pass

    def end(self, interrupted):
        pass

    def isFinished(self):
        return (self.instant or self.grabbersub.is_at_setpoint())
