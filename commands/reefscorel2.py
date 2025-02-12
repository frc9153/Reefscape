import commands2

from constants import LiftConstants, JointConstants, GrabberConstants
from subsystems.liftsubsytem import LiftSubsystem
from subsystems.jointsubsystem import JointSubsystem
from subsystems.grabbersubsystem import GrabberSubsystem
from commands.lifttosetpoint import LiftToSetpoint
from commands.jointtosetpoint import JointToSetpoint
from rev import CANSparkMax, SparkMaxAbsoluteEncoder, CANSparkLowLevel

class ReefScoreL2(commands2.SequentialCommandGroup):
    def __init__(self, liftsub, jointsub, grabbersub):
        super().__init__()

        self.liftsub = liftsub
        self.jointsub = jointsub
        self.grabbersub = grabbersub

        # self.lift_store = commands2.cmd.runOnce(
        #     lambda: self.liftsub.go_to_setpoint(
        #         LiftConstants.setpoint_store
        #     ),
        #     self.liftsub
        # )

        # self.lift_l4 = commands2.cmd.runOnce(
        #     lambda: self.liftsub.go_to_setpoint(
        #         LiftConstants.setpoint_l4
        #     ),
        #     self.liftsub
        # )
        
        # self.joint_intake_for_good_measure = commands2.cmd.runOnce(
        #     lambda: self.jointsub.go_to_setpoint(
        #         JointConstants.setpoint_intake
        #     ),
        #     self.jointsub
        # )
        
        # self.joint_intake = commands2.cmd.runOnce(
        #     lambda: self.jointsub.go_to_setpoint(
        #         JointConstants.setpoint_intake
        #     ),
        #     self.jointsub
        # )
        
        # self.joint_scorehigh = commands2.cmd.runOnce(
        #     lambda: self.jointsub.go_to_setpoint(
        #         JointConstants.setpoint_scorehigh
        #     ),
        #     self.jointsub
        # )
        
        self.grabber_release = commands2.cmd.runOnce(
            lambda: self.grabbersub.go_to_setpoint(
                GrabberConstants.setpoint_open
            ),
            self.grabbersub
        )

        # Cannot schedule same command twice
        self.addCommands(JointToSetpoint(self.jointsub, JointConstants.setpoint_intake),
                        LiftToSetpoint(self.liftsub, LiftConstants.setpoint_l2),
                        JointToSetpoint(self.jointsub, JointConstants.setpoint_scorel2),
                        self.grabber_release,
                        JointToSetpoint(self.jointsub, JointConstants.setpoint_intake),
                        LiftToSetpoint(self.liftsub, LiftConstants.setpoint_store)
        )
    
    # DO NOT ADD ANY OF THE FOLLOWING:
    #       Initialize
    #       Execute
    #       IsFinished
    #       End
    # ON PAIN OF DEATH BY ROBOT ARM