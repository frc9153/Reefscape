import commands2

from constants import AlgaeConstants
from subsystems.algaesubsystem import AlgaeSubsystem

class AlgaeToSetpoint(commands2.Command):

    def __init__(self, algaesub, setpoint):
        self.algaesub = algaesub
        self.setpoint = setpoint

    def initialize(self):
        self.algaesub.go_to_setpoint(self.setpoint)

    def execute(self):
        pass

    def end(self, interrupted):
        pass

    def isFinished(self):
        return self.liftsub.is_at_setpoint()
