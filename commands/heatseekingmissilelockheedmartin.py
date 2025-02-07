import commands2

from constants import AlgaeConstants
from subsystems.algaesubsystem import AlgaeSubsystem
from rev import CANSparkMax, SparkMaxAbsoluteEncoder, CANSparkLowLevel
from subsystems.drivesubsystem import DriveSubsystem

class HeatSeekingMissileLockheedMartin(commands2.Command):
    def __init__(self, drive_sub: DriveSubsystem):
        super().__init__()
        self.drive_sub = drive_sub
    
    def periodic(self) -> None:
        pass
    
    def isFinished(self):
        return self.algaesub.encoder.getPosition() < AlgaeConstants.consumed_threshold
    
    def end(self, interrupted):
        self.algaesub.set_chomp_power(AlgaeConstants.stoptake_speed)
        self.algaesub.motor_raise.setIdleMode(CANSparkMax.IdleMode.kBrake)
        