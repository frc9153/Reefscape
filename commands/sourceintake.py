import commands2

from constants import LiftConstants, JointConstants, GrabberConstants
from subsystems.liftsubsytem import LiftSubsystem
from subsystems.jointsubsystem import JointSubsystem
from subsystems.grabbersubsystem import GrabberSubsystem
from commands.lifttosetpoint import LiftToSetpoint
from commands.jointtosetpoint import JointToSetpoint
from commands.grabbertosetpoint import GrabberToSetpoint

class SourceIntake(commands2.SequentialCommandGroup):
    def __init__(self, liftsub, jointsub, grabbersub, robotDrive):
        super().__init__()

        self.liftsub = liftsub
        self.jointsub = jointsub
        self.grabbersub = grabbersub
        self.robotDrive = robotDrive # Merely to interrupt driving

        # Cannot schedule same command twice
        self.addCommands(JointToSetpoint(self.jointsub, JointConstants.setpoint_store),
                        LiftToSetpoint(self.liftsub, LiftConstants.setpoint_intake),
                        GrabberToSetpoint(self.grabbersub, GrabberConstants.setpoint_intake, False),
                        JointToSetpoint(self.jointsub, JointConstants.setpoint_intake))
    
    # DO NOT ADD ANY OF THE FOLLOWING:
    #       Initialize
    #       Execute
    #       IsFinished
    #       End
    # ON PAIN OF DEATH BY ROBOT ARM