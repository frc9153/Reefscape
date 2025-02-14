import commands2

from constants import AutoConstants
from subsystems.liftsubsytem import LiftSubsystem
from subsystems.jointsubsystem import JointSubsystem
from subsystems.grabbersubsystem import GrabberSubsystem
from subsystems.drivesubsystem import DriveSubsystem
from subsystems.transformablegyro import TransformableGyro

from commands.drivecommand import DriveCommand

class Mobility(commands2.SequentialCommandGroup):
    def __init__(self, liftsub: LiftSubsystem, jointsub: JointSubsystem, grabbersub: GrabberSubsystem, drivesub: DriveSubsystem, robot_gyro):
        super().__init__()

        self.reset_gyro = commands2.cmd.runOnce(
            lambda: self.robot_gyro.reset(),
            self.robot_gyro
        )

        mobility_time = AutoConstants.mobility_dist*AutoConstants.power_time_per_inch/AutoConstants.robot_speed

        # Cannot schedule same command twice
        self.addCommands(
            self.reset_gyro,
            DriveCommand(drivesub, 0.0, AutoConstants.robot_speed, 0.0, False).withTimeout(mobility_time)
        )
    
    # DO NOT ADD ANY OF THE FOLLOWING:
    #       Initialize
    #       Execute
    #       IsFinished
    #       End
    # ON PAIN OF DEATH BY ROBOT ARM