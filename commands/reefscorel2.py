import commands2

from constants import LiftConstants, JointConstants, GrabberConstants
from subsystems.liftsubsytem import LiftSubsystem
from subsystems.jointsubsystem import JointSubsystem
from subsystems.grabbersubsystem import GrabberSubsystem
from subsystems.drivesubsystem import DriveSubsystem

from commands.lifttosetpoint import LiftToSetpoint
from commands.jointtosetpoint import JointToSetpoint
from commands.grabbertosetpoint import GrabberToSetpoint

class ReefScoreL2(commands2.SequentialCommandGroup):
    def __init__(self, liftsub: LiftSubsystem, jointsub: JointSubsystem, grabbersub: GrabberSubsystem, drivesub: DriveSubsystem):
        super().__init__()

        # Cannot schedule same command twice
        self.addCommands(JointToSetpoint(jointsub, JointConstants.setpoint_store),
                        LiftToSetpoint(liftsub, LiftConstants.setpoint_l2),
                        JointToSetpoint(jointsub, JointConstants.setpoint_scorel2),
                        GrabberToSetpoint(grabbersub, GrabberConstants.setpoint_open, True),
                        JointToSetpoint(jointsub, JointConstants.setpoint_store),
                        LiftToSetpoint(liftsub, LiftConstants.setpoint_store)
        )
    
    # DO NOT ADD ANY OF THE FOLLOWING:
    #       Initialize
    #       Execute
    #       IsFinished
    #       End
    # ON PAIN OF DEATH BY ROBOT ARM