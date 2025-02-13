from commands2 import Subsystem
from constants import LiftConstants
from rev import CANSparkMax, SparkMaxAbsoluteEncoder, CANSparkLowLevel


class LiftSubsystem(Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.motor_one = CANSparkMax(
            LiftConstants.motor_one, CANSparkMax.MotorType.kBrushless
        )

        self.motor_two = CANSparkMax(
            LiftConstants.motor_two, CANSparkMax.MotorType.kBrushless
        )

        self.motor_two.follow(self.motor_one, True)

        # self.limit_switch = self.motor_one.getForwardLimitSwitch()

        self.PID_controller = self.motor_one.getPIDController()
        self.encoder = self.motor_one.getAbsoluteEncoder(
            SparkMaxAbsoluteEncoder.Type.kDutyCycle
        )
        
        self.encoder.setInverted(True)
        
        self.PID_controller.setP(LiftConstants.P)
        self.PID_controller.setI(LiftConstants.I)
        self.PID_controller.setD(LiftConstants.D)
        self.PID_controller.setIZone(LiftConstants.i_zone)
        self.PID_controller.setFF(LiftConstants.Ff)

        self.PID_controller.setOutputRange(
            -LiftConstants.max_speed_motor,
            LiftConstants.max_speed_motor
        )
        self.PID_controller.setFeedbackDevice(self.encoder)

        self.motor_one.setIdleMode(CANSparkMax.IdleMode.kBrake)
        self.motor_one.burnFlash()

        self.motor_two.setIdleMode(CANSparkMax.IdleMode.kBrake)
        self.motor_two.burnFlash()

        self.setpoint = 0.0

    def go_to_setpoint(self, setpoint):
        self.setpoint = setpoint
        self.PID_controller.setReference(setpoint, CANSparkLowLevel.ControlType.kPosition)

    def set_motor_power(self, power):
        self.motor_one.set(power)

    def is_at_setpoint(self):
        return abs(self.setpoint - self.encoder.getPosition()) <= LiftConstants.PIDEpsilon
    
    def is_at_lowest(self):
        return (self.setpoint == LiftConstants.setpoint_store)

    def periodic(self):
        pass
        # if self.limit_switch.get():
        #     self.motor_one.set(0)