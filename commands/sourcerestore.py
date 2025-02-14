import commands2

from constants import LiftConstants, JointConstants, GrabberConstants
from subsystems.liftsubsytem import LiftSubsystem
from subsystems.jointsubsystem import JointSubsystem
from subsystems.grabbersubsystem import GrabberSubsystem
from subsystems.drivesubsystem import DriveSubsystem

from commands.lifttosetpoint import LiftToSetpoint
from commands.jointtosetpoint import JointToSetpoint
from commands.grabbertosetpoint import GrabberToSetpoint
from commands.grabbergrabreset import GrabberGrabReset
from commands.drivecommand import DriveCommand

class SourceRestore(commands2.SequentialCommandGroup):
    def __init__(self, liftsub: LiftSubsystem, jointsub: JointSubsystem, grabbersub: GrabberSubsystem, drivesub: DriveSubsystem):
        super().__init__()

        # Cannot schedule same command twice
        self.addCommands(GrabberToSetpoint(grabbersub, GrabberConstants.setpoint_intake2, False),
                        DriveCommand(drivesub, 0.0, -0.1, 0.0, False).withTimeout(0.2),
                        GrabberGrabReset(grabbersub),
                        JointToSetpoint(jointsub, JointConstants.setpoint_store))
    
    # DO NOT ADD ANY OF THE FOLLOWING:
    #       Initialize
    #       Execute
    #       IsFinished
    #       End
    # ON PAIN OF DEATH BY ROBOT ARM