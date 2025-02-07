import commands2

from constants import LiftConstants, JointConstants, GrabberConstants
from subsystems.liftsubsytem import LiftSubsystem
from subsystems.jointsubsystem import JointSubsystem
from subsystems.grabbersubsystem import GrabberSubsystem
from rev import CANSparkMax, SparkMaxAbsoluteEncoder, CANSparkLowLevel

class ReefScoreL4(commands2.SequentialCommandGroup):
    def __init__(self, liftsub, jointsub, grabbersub):
        super().__init__()

        self.liftsub = liftsub
        self.jointsub = jointsub
        self.grabbersub = grabbersub

        self.lift_store = commands2.cmd.runOnce(
            lambda: self.liftsub.go_to_setpoint(
                LiftConstants.setpoint_store
            ),
            self.liftsub
        )

        self.lift_l4 = commands2.cmd.runOnce(
            lambda: self.liftsub.go_to_setpoint(
                LiftConstants.setpoint_l4
            ),
            self.liftsub
        )
        
        self.joint_intake_for_good_measure = commands2.cmd.runOnce(
            lambda: self.jointsub.go_to_setpoint(
                JointConstants.setpoint_intake
            ),
            self.jointsub
        )
        
        self.joint_intake = commands2.cmd.runOnce(
            lambda: self.jointsub.go_to_setpoint(
                JointConstants.setpoint_intake
            ),
            self.jointsub
        )
        
        self.joint_scorehigh = commands2.cmd.runOnce(
            lambda: self.jointsub.go_to_setpoint(
                JointConstants.setpoint_scorehigh
            ),
            self.jointsub
        )
        
        self.grabber_release = commands2.cmd.runOnce(
            lambda: self.grabbersub.go_to_setpoint(
                GrabberConstants.setpoint_open
            ),
            self.grabbersub
        )

        # Cannot schedule same command twice
        self.addCommands(self.joint_intake_for_good_measure,
                        self.lift_l4,
                        self.joint_scorehigh,
                        self.grabber_release,
                        self.joint_intake,
                        self.lift_store)
    
    def initialize(self):
        pass
        # self.algaesub.set_chomp_power(AlgaeConstants.intake_speed)
        # self.algaesub.kill_PID()
        # self.algaesub.motor_raise.setIdleMode(CANSparkMax.IdleMode.kCoast)

    def isFinished(self):
        pass
        # return self.algaesub.encoder.getPosition() < AlgaeConstants.consumed_threshold
    
    def end(self, interrupted):
        pass
        # self.algaesub.set_chomp_power(AlgaeConstants.stoptake_speed)
        # self.algaesub.motor_raise.setIdleMode(CANSparkMax.IdleMode.kBrake)
        