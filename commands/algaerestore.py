import commands2

from constants import LiftConstants, AlgaeConstants
from subsystems.liftsubsytem import LiftSubsystem
from subsystems.algaesubsystem import AlgaeSubsystem
from commands.wowimfull import WowImFull
from commands.lifttosetpoint import LiftToSetpoint
from commands.algaetosetpoint import AlgaeToSetpoint

class AlgaeRestore(commands2.SequentialCommandGroup):
    def __init__(self, liftsub, algaesub):
        super().__init__()

        self.liftsub = liftsub
        self.algaesub = algaesub

        # Cannot schedule same command twice

        if (self.liftsub.is_at_lowest()):
            self.addCommands(LiftToSetpoint(self.liftsub, LiftConstants.setpoint_l2))

        self.addCommands(AlgaeToSetpoint(self.algaesub, AlgaeConstants.setpoint_up),
                        LiftToSetpoint(self.liftsub, LiftConstants.setpoint_store))
    
    # DO NOT ADD ANY OF THE FOLLOWING:
    #       Initialize
    #       Execute
    #       IsFinished
    #       End
    # ON PAIN OF DEATH BY ROBOT ARM