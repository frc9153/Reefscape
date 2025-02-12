import math
import commands2

from constants import HeatSeekingMissileLockheedMartinConstants
from subsystems.drivesubsystem import DriveSubsystem
import limelight

class HeatSeekingMissileLockheedMartin(commands2.Command):
    def __init__(self, drive_sub: DriveSubsystem):
        super().__init__()
        self.drive_sub = drive_sub
    
    def execute(self) -> None:
        self.drive_sub.drive(limelight.get_tx(), 0.0, 0.0, False, False)
    
    def isFinished(self):
        return math.abs(limelight.get_tx()) < HeatSeekingMissileLockheedMartinConstants.apriltag_position_threshold
    
    def end(self, interrupted):
        self.drive_sub.drive(0.0, 0.0, 0.0, False, False)
        