import commands2

from constants import AlgaeConstants
from subsystems.algaesubsystem import AlgaeSubsystem
from rev import CANSparkMax, SparkMaxAbsoluteEncoder, CANSparkLowLevel

class WowImFull(commands2.Command):
    def __init__(self, algaesub: AlgaeSubsystem):
        super().__init__()

        self.algaesub = algaesub
    
    def initialize(self):
        self.algaesub.set_chomp_power(AlgaeConstants.intake_speed)
        self.algaesub.kill_PID()
        self.algaesub.motor_raise.setIdleMode(CANSparkMax.IdleMode.kCoast)

    def isFinished(self):
        return self.algaesub.encoder.getPosition() < AlgaeConstants.consumed_threshold
    
    def end(self, interrupted):
        self.algaesub.set_chomp_power(AlgaeConstants.stoptake_speed)
        self.algaesub.motor_raise.setIdleMode(CANSparkMax.IdleMode.kBrake)
        