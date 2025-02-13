from commands2 import Subsystem
from constants import JointConstants
from rev import CANSparkMax, SparkMaxAbsoluteEncoder, CANSparkLowLevel


class JointSubsystem(Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.motor = CANSparkMax(
            JointConstants.motor, CANSparkMax.MotorType.kBrushless
        )

        self.PID_controller = self.motor.getPIDController()
        self.encoder = self.motor.getAbsoluteEncoder(
            SparkMaxAbsoluteEncoder.Type.kDutyCycle
            )
        
        self.encoder.setInverted(True)
        
        self.PID_controller.setP(JointConstants.P)
        self.PID_controller.setI(JointConstants.I)
        self.PID_controller.setD(JointConstants.D)
        self.PID_controller.setIZone(JointConstants.i_zone)
        self.PID_controller.setFF(JointConstants.Ff)

        self.PID_controller.setOutputRange(
            -JointConstants.max_speed_motor,
            JointConstants.max_speed_motor
        )
        self.PID_controller.setFeedbackDevice(self.encoder)

        self.motor.setIdleMode(CANSparkMax.IdleMode.kBrake)
        self.motor.burnFlash()
        
        self.setpoint = 0.0

    def go_to_setpoint(self, setpoint):
        self.setpoint = setpoint
        self.PID_controller.setReference(setpoint, CANSparkLowLevel.ControlType.kPosition)
        
    def is_at_setpoint(self):
        return abs(self.setpoint - self.encoder.getPosition()) <= JointConstants.PIDEpsilon