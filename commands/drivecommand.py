import commands2

from constants import DriveConstants
from subsystems.drivesubsystem import DriveSubsystem

class DriveCommand(commands2.Command):

    def __init__(self, drivesub: DriveSubsystem, x_speed: float, y_speed: float, rotation: float, field_relative: bool):
        self.drivesub = drivesub
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rotation = rotation
        self.field_relative = field_relative

    def initialize(self):
        self.drivesub.drive(self.x_speed, self.y_speed, self.rotation, self.field_relative, False)

    def execute(self):
        pass

    def end(self, interrupted):
        self.drivesub.drive(0.0, 0.0, 0.0, False, False)

    def isFinished(self):
        return False
