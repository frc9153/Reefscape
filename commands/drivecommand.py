import commands2

from constants import DriveConstants
from subsystems.drivesubsystem import DriveSubsystem

class DriveCommand(commands2.Command):

    def __init__(self, robotDrive, x_speed, y_speed, rotation, field_relative):
        self.robotDrive = robotDrive
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rotation = rotation
        self.field_relative = field_relative

    def initialize(self):
        self.robotDrive.drive(self.x_speed, self.y_speed, self.rotation, self.field_relative, False)

    def execute(self):
        pass

    def end(self, interrupted):
        self.robotDrive.drive(0.0, 0.0, 0.0, False, False)

    def isFinished(self):
        return False
