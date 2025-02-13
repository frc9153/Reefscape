import commands2

from constants import LiftConstants, JointConstants, GrabberConstants
from subsystems.liftsubsytem import LiftSubsystem
from subsystems.jointsubsystem import JointSubsystem
from subsystems.grabbersubsystem import GrabberSubsystem
from commands.lifttosetpoint import LiftToSetpoint
from commands.jointtosetpoint import JointToSetpoint
from commands.drivecommand import DriveCommand

class ReefBludgeonHigh(commands2.SequentialCommandGroup):
    def __init__(self, liftsub, jointsub, grabbersub, robotDrive):
        super().__init__()

        self.liftsub = liftsub
        self.jointsub = jointsub
        self.grabbersub = grabbersub
        self.robotDrive = robotDrive

        self.joint_bludgeon = commands2.cmd.runOnce(
            lambda: self.jointsub.set_power(
                JointConstants.bludgeon_speed
            ),
            self.jointsub
        )

        self.joint_end_bludgeon = commands2.cmd.runOnce(
            lambda: self.jointsub.set_power(
                JointConstants.bludgeon_speed
            ),
            self.jointsub
        )

        # Cannot schedule same command twice
        self.addCommands(JointToSetpoint(self.jointsub, JointConstants.setpoint_bludgeon),
                        LiftToSetpoint(self.liftsub, LiftConstants.setpoint_bludgeon_high),
                        self.joint_bludgeon,
                        DriveCommand(self.robotDrive, 0.0, -0.1, 0.0, False).withTimeout(0.2),
                        self.joint_end_bludgeon,
                        JointToSetpoint(self.jointsub, JointConstants.setpoint_store))
    
    # DO NOT ADD ANY OF THE FOLLOWING:
    #       Initialize
    #       Execute
    #       IsFinished
    #       End
    # ON PAIN OF DEATH BY ROBOT ARM