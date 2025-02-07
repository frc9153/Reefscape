from commands2 import Subsystem
from constants import GrabberConstants
from rev import CANSparkMax, SparkMaxAbsoluteEncoder, CANSparkLowLevel


class GrabberSubsystem(Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.motor = CANSparkMax(
            GrabberConstants.motor, CANSparkMax.MotorType.kBrushless
        )

        self.PID_controller = self.motor.getPIDController()
        # self.encoder = self.motor.getAbsoluteEncoder(
        #     SparkMaxAbsoluteEncoder.Type.kDutyCycle
        #     )
        
        self.PID_controller.setP(GrabberConstants.P)
        self.PID_controller.setI(GrabberConstants.I)
        self.PID_controller.setD(GrabberConstants.D)
        self.PID_controller.setIZone(GrabberConstants.i_zone)
        self.PID_controller.setFF(GrabberConstants.Ff)

        self.PID_controller.setOutputRange(
            -GrabberConstants.max_speed_motor,
            GrabberConstants.max_speed_motor
        )
        # self.PID_controller.setFeedbackDevice(self.encoder)

        self.motor.setIdleMode(CANSparkMax.IdleMode.kBrake)
        self.motor.burnFlash()

    def go_to_setpoint(self, setpoint):
        self.PID_controller.setReference(setpoint, CANSparkLowLevel.ControlType.kPosition)
    
    def set_power(self, power):
        self.motor.set(power)