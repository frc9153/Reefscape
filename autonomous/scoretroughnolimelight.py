import commands2

from constants import AutoConstants, HeatSeekingMissileLockheedMartinConstants
from subsystems.liftsubsytem import LiftSubsystem
from subsystems.jointsubsystem import JointSubsystem
from subsystems.grabbersubsystem import GrabberSubsystem
from subsystems.drivesubsystem import DriveSubsystem
from subsystems.transformablegyro import TransformableGyro

from commands.reefscorel2 import ReefScoreL2

class ScoreTroughNoLimelight(commands2.SequentialCommandGroup):
    def __init__(self, liftsub: LiftSubsystem, jointsub: JointSubsystem, grabbersub: GrabberSubsystem, drivesub: DriveSubsystem, robot_gyro: TransformableGyro):
        super().__init__()

        # Routine: -1, 0, 1 for left, center, right

        # Cannot schedule same command twice
        self.addCommands(
            ReefScoreL2(liftsub, jointsub, grabbersub, drivesub)
        )
    
    # DO NOT ADD ANY OF THE FOLLOWING:
    #       Initialize
    #       Execute
    #       IsFinished
    #       End
    # ON PAIN OF DEATH BY ROBOT ARM