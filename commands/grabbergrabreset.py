import commands2

from constants import GrabberConstants
from subsystems.grabbersubsystem import GrabberSubsystem

class GrabberGrabReset(commands2.SequentialCommandGroup):
    def __init__(self, grabbersub: GrabberSubsystem):
        super().__init__()
        
        self.grabber_grab = commands2.cmd.runOnce(
            lambda: grabbersub.set_power(GrabberConstants.hold_speed),
            grabbersub
        )
        self.grabber_reset = commands2.cmd.runOnce(
            lambda: grabbersub.reset_encoder(),
            grabbersub
        )

        # Cannot schedule same command twice
        self.addCommands(self.grabber_grab,
                        commands2.WaitCommand(0.2),
                        self.grabber_reset)
    
    # DO NOT ADD ANY OF THE FOLLOWING:
    #       Initialize
    #       Execute
    #       IsFinished
    #       End
    # ON PAIN OF DEATH BY ROBOT ARM