import math
import commands2

from constants import HeatSeekingMissileLockheedMartinConstants
from subsystems.drivesubsystem import DriveSubsystem
import limelight

class HeatSeekingMissileLockheedMartinTarget(commands2.Command):
    def __init__(self, drive_sub: DriveSubsystem, speed: float, offset: float):
        super().__init__()
        self.drive_sub = drive_sub
        self.speed = speed
        self.offset = offset
    
    def execute(self) -> None:
        self.drive_sub.drive(0.0, self.speed, (limelight.get_tx()-self.offset), False, False)
    
    def isFinished(self):
        pass
        # return math.abs(limelight.get_tx()) < HeatSeekingMissileLockheedMartinConstants.apriltag_position_threshold
    
    def end(self, interrupted):
        self.drive_sub.drive(0.0, 0.0, 0.0, False, False)
        