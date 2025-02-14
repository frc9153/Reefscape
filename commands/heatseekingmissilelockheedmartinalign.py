import math
import commands2

from constants import HeatSeekingMissileLockheedMartinConstants
from subsystems.drivesubsystem import DriveSubsystem
import limelight

class HeatSeekingMissileLockheedMartinAlign(commands2.Command):
    def __init__(self, drive_sub: DriveSubsystem, offset: float):
        super().__init__()
        self.drive_sub = drive_sub
        self.offset = offset
    
    def execute(self) -> None:
        self.drive_sub.drive((limelight.get_tx()-self.offset), 0.0, 0.0, False, False)
    
    def isFinished(self):
        return math.abs(limelight.get_tx()-self.offset) < HeatSeekingMissileLockheedMartinConstants.apriltag_position_threshold
    
    def end(self, interrupted):
        self.drive_sub.drive(0.0, 0.0, 0.0, False, False)
        