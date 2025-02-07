from commands2 import Subsystem
from constants import AlgaeConstants
from rev import CANSparkMax, SparkMaxAbsoluteEncoder, CANSparkLowLevel


class AlgaeSubsystem(Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.motor_raise = CANSparkMax(
            AlgaeConstants.motor_raise, CANSparkMax.MotorType.kBrushless
        )

        self.motor_eat = CANSparkMax(
            AlgaeConstants.motor_eat, CANSparkMax.MotorType.kBrushless
        )

        # self.motor_raise.setInverted(True)

        self.PID_controller = self.motor_raise.getPIDController()
        self.encoder = self.motor_raise.getAbsoluteEncoder(
            SparkMaxAbsoluteEncoder.Type.kDutyCycle
            )
        
        self.encoder.setInverted(True)
        
        self.PID_controller.setP(AlgaeConstants.P)
        self.PID_controller.setI(AlgaeConstants.I)
        self.PID_controller.setD(AlgaeConstants.D)
        self.PID_controller.setIZone(AlgaeConstants.i_zone)
        self.PID_controller.setFF(AlgaeConstants.Ff)

        self.PID_controller.setOutputRange(
            -AlgaeConstants.max_speed_motor,
            AlgaeConstants.max_speed_motor
        )
        self.PID_controller.setFeedbackDevice(self.encoder)

        self.motor_raise.setIdleMode(CANSparkMax.IdleMode.kBrake)
        self.motor_raise.burnFlash()

    def go_to_setpoint(self, setpoint):
        self.PID_controller.setReference(setpoint, CANSparkLowLevel.ControlType.kPosition)

    def kill_PID(self):
        self.motor_raise.set(0)

    def set_chomp_power(self, power):
        self.motor_eat.set(power)