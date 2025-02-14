
from commands2 import Subsystem
import navx
import wpilib

class TransformableGyro(Subsystem):

    def __init__(self):
        self.gyro = navx.AHRS(wpilib.SPI.Port.kMXP)
        self.rotation_offset = 0.0

    def get_angle(self):
        return (self.gyro.getAngle()-self.rotation_offset+360) % 360

    def reset(self):
        self.gyro.reset()
        self.rotation_offset = 0.0

    def fakeReset(self, angle):
        self.gyro.reset()
        self.rotation_offset = angle
