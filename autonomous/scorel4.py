import commands2

from constants import AutoConstants, HeatSeekingMissileLockheedMartinConstants
from subsystems.liftsubsytem import LiftSubsystem
from subsystems.jointsubsystem import JointSubsystem
from subsystems.grabbersubsystem import GrabberSubsystem
from subsystems.drivesubsystem import DriveSubsystem
from subsystems.transformablegyro import TransformableGyro

from commands.reefscorel4 import ReefScoreL4
from commands.heatseekingmissilelockheedmartinalign import HeatSeekingMissileLockheedMartinAlign

class ScoreL4(commands2.SequentialCommandGroup):
    def __init__(self, liftsub: LiftSubsystem, jointsub: JointSubsystem, grabbersub: GrabberSubsystem, drivesub: DriveSubsystem, robot_gyro: TransformableGyro, side: int):
        super().__init__()

        # Side: -1, 1 for left, right

        # Cannot schedule same command twice
        self.addCommands(
            HeatSeekingMissileLockheedMartinAlign(drivesub, HeatSeekingMissileLockheedMartinConstants.offsets[side+1]),
            ReefScoreL4(liftsub, jointsub, grabbersub, drivesub)
        )
    
    # DO NOT ADD ANY OF THE FOLLOWING:
    #       Initialize
    #       Execute
    #       IsFinished
    #       End
    # ON PAIN OF DEATH BY ROBOT ARM