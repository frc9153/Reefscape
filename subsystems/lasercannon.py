from commands2 import Subsystem

import au.grapplerobotics.ConfigurationFailedException
import au.grapplerobotics.LaserCan
from constants import LaserConstants

class LaserCannon(Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.laserCan = LaserCan(LaserConstants.laserCannonId)

        # Optionally initialise the settings of the LaserCAN, if you haven't already done so in GrappleHook
        try:
            self.laserCan.setRangingMode(LaserCan.RangingMode.SHORT)
            self.laserCan.setRegionOfInterest(LaserCan.RegionOfInterest(8, 8, 16, 16))
            self.laserCan.setTimingBudget(LaserCan.TimingBudget.TIMING_BUDGET_33MS)
        except(e):
            print("Configuration failed! " + e)
    
    def getDistance(self):
        measurement = self.laserCan.getMeasurement()
        if (measurement == null or measurement.status != LaserCan.LASERCAN_STATUS_VALID_MEASUREMENT):
            print("Sensor Data Invalid")
        return measurement.distance_mm

    def sensorTriggered(self):
        if (self.getDistance() < LaserConstants.noteDistThreshold):
            return True
        return False

    # def periodic(self):
        # SmartDashboard.putNumber("LaserCannon Dist", self.getDistance())