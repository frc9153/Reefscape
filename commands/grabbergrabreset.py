import commands2

from constants import GrabberConstants
from subsystems.grabbersubsystem import GrabberSubsystem

class GrabberGrabReset(commands2.SequentialCommandGroup):
    def __init__(self, grabbersub):
        super().__init__()

        self.grabbersub = grabbersub
        
        self.grabber_grab = commands2.cmd.runOnce(
            lambda: self.grabbersub.set_power(GrabberConstants.hold_speed),
            self.grabbersub
        )
        self.grabber_reset = commands2.cmd.runOnce(
            lambda: self.grabbersub.reset_encoder,
            self.grabbersub
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