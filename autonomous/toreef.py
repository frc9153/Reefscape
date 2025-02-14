import commands2

from constants import AutoConstants
from subsystems.liftsubsytem import LiftSubsystem
from subsystems.jointsubsystem import JointSubsystem
from subsystems.grabbersubsystem import GrabberSubsystem
from subsystems.drivesubsystem import DriveSubsystem
from subsystems.transformablegyro import TransformableGyro

from commands.heatseekingmissilelockheedmartintarget import HeatSeekingMissileLockheedMartinTarget

class ToReef(commands2.SequentialCommandGroup):
    def __init__(self, liftsub: LiftSubsystem, jointsub: JointSubsystem, grabbersub: GrabberSubsystem, drivesub: DriveSubsystem, robot_gyro: TransformableGyro, routine: int):
        super().__init__()

        # Routine: -1, 0, 1 for left, center, right

        self.reset_gyro = commands2.cmd.runOnce(
            lambda: self.robot_gyro.fakeReset(60*routine),
            self.robot_gyro
        )

        reef_time = AutoConstants.reef_dist[routine+1]*AutoConstants.power_time_per_inch/AutoConstants.robot_speed

        # Cannot schedule same command twice
        self.addCommands(
            HeatSeekingMissileLockheedMartinTarget(drivesub, AutoConstants.robot_speed, 0.0).withTimeout(reef_time),
            self.reset_gyro,
        )
    
    # DO NOT ADD ANY OF THE FOLLOWING:
    #       Initialize
    #       Execute
    #       IsFinished
    #       End
    # ON PAIN OF DEATH BY ROBOT ARM