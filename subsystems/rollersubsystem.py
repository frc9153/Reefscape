from commands2 import Subsystem
from constants import RollerConstants
from rev import CANSparkMax, SparkMaxAbsoluteEncoder, CANSparkLowLevel


class RollerSubsystem(Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.motor = CANSparkMax(
            RollerConstants.motor_id, CANSparkMax.MotorType.kBrushless
        )

        self.motor.setIdleMode(CANSparkMax.IdleMode.kBrake)
        self.motor.burnFlash()

    def set_power(self, power):
        print(power)
        self.motor.set(power)