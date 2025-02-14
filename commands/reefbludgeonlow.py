import commands2

from constants import LiftConstants, JointConstants, GrabberConstants
from subsystems.liftsubsytem import LiftSubsystem
from subsystems.jointsubsystem import JointSubsystem
from subsystems.grabbersubsystem import GrabberSubsystem
from subsystems.drivesubsystem import DriveSubsystem

from commands.lifttosetpoint import LiftToSetpoint
from commands.jointtosetpoint import JointToSetpoint
from commands.drivecommand import DriveCommand

class ReefBludgeonLow(commands2.SequentialCommandGroup):
    def __init__(self, liftsub: LiftSubsystem, jointsub: JointSubsystem, grabbersub: GrabberSubsystem, drivesub: DriveSubsystem):
        super().__init__()

        self.joint_bludgeon = commands2.cmd.runOnce(
            lambda: jointsub.set_power(
                JointConstants.bludgeon_speed
            ),
            jointsub
        )

        self.joint_end_bludgeon = commands2.cmd.runOnce(
            lambda: jointsub.set_power(
                JointConstants.bludgeon_speed
            ),
            jointsub
        )

        # Cannot schedule same command twice
        self.addCommands(JointToSetpoint(jointsub, JointConstants.setpoint_bludgeon),
                        LiftToSetpoint(liftsub, LiftConstants.setpoint_bludgeon_low),
                        self.joint_bludgeon,
                        DriveCommand(drivesub, 0.0, -0.1, 0.0, False).withTimeout(0.2),
                        self.joint_end_bludgeon,
                        JointToSetpoint(jointsub, JointConstants.setpoint_store))
    
    # DO NOT ADD ANY OF THE FOLLOWING:
    #       Initialize
    #       Execute
    #       IsFinished
    #       End
    # ON PAIN OF DEATH BY ROBOT ARM