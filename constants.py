# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.

"""
The constants module is a convenience place for teams to hold robot-wide
numerical or boolean constants. Don't use this for any other purpose!
"""


import math

from wpimath import units
from wpimath.geometry import Translation2d
from wpimath.kinematics import SwerveDrive4Kinematics
from wpimath.trajectory import TrapezoidProfileRadians

from rev import CANSparkMax


class NeoMotorConstants:
    kFreeSpeedRpm = 5676


class DriveConstants:
    # Driving Parameters - Note that these are not the maximum capable speeds of
    # the robot, rather the allowed maximum speeds
    kMaxSpeedMetersPerSecond = 4.8
    kMaxAngularSpeed = math.tau  # radians per second

    kDirectionSlewRate = 1.2  # radians per second
    kMagnitudeSlewRate = 1.8  # percent per second (1 = 100%)
    kRotationalSlewRate = 2.0  # percent per second (1 = 100%)

    # Chassis configuration
    kTrackWidth = units.inchesToMeters(26.5)
    # Distance between centers of right and left wheels on robot
    kWheelBase = units.inchesToMeters(26.5)

    # Distance between front and back wheels on robot
    kModulePositions = [
        Translation2d(kWheelBase / 2, kTrackWidth / 2),
        Translation2d(kWheelBase / 2, -kTrackWidth / 2),
        Translation2d(-kWheelBase / 2, kTrackWidth / 2),
        Translation2d(-kWheelBase / 2, -kTrackWidth / 2),
    ]
    kDriveKinematics = SwerveDrive4Kinematics(*kModulePositions)

    # Angular offsets of the modules relative to the chassis in radians
    kFrontLeftChassisAngularOffset = -math.pi / 2
    kFrontRightChassisAngularOffset = 0
    kBackLeftChassisAngularOffset = math.pi
    kBackRightChassisAngularOffset = math.pi / 2

    # SPARK MAX CAN IDs
    kFrontLeftDrivingCanId = 7
    kRearLeftDrivingCanId = 5
    kFrontRightDrivingCanId = 1
    kRearRightDrivingCanId = 3

    kFrontLeftTurningCanId = 8
    kRearLeftTurningCanId = 6
    kFrontRightTurningCanId = 2
    kRearRightTurningCanId = 4

    kGyroReversed = False


class ModuleConstants:
    # The MAXSwerve module can be configured with one of three pinion gears: 12T, 13T, or 14T.
    # This changes the drive speed of the module (a pinion gear with more teeth will result in a
    # robot that drives faster).
    kDrivingMotorPinionTeeth = 14

    # Invert the turning encoder, since the output shaft rotates in the opposite direction of
    # the steering motor in the MAXSwerve Module.
    kTurningEncoderInverted = True

    # Calculations required for driving motor conversion factors and feed forward
    kDrivingMotorFreeSpeedRps = NeoMotorConstants.kFreeSpeedRpm / 60
    kWheelDiameterMeters = 0.0762
    kWheelCircumferenceMeters = kWheelDiameterMeters * math.pi
    # 45 teeth on the wheel's bevel gear, 22 teeth on the first-stage spur gear, 15 teeth on the bevel pinion
    kDrivingMotorReduction = (45.0 * 22) / (kDrivingMotorPinionTeeth * 15)
    kDriveWheelFreeSpeedRps = (
        kDrivingMotorFreeSpeedRps * kWheelCircumferenceMeters
    ) / kDrivingMotorReduction

    kDrivingEncoderPositionFactor = (
        kWheelDiameterMeters * math.pi
    ) / kDrivingMotorReduction  # meters
    kDrivingEncoderVelocityFactor = (
        (kWheelDiameterMeters * math.pi) / kDrivingMotorReduction
    ) / 60.0  # meters per second

    kTurningEncoderPositionFactor = math.tau  # radian
    kTurningEncoderVelocityFactor = math.tau / 60.0  # radians per second

    kTurningEncoderPositionPIDMinInput = 0  # radian
    kTurningEncoderPositionPIDMaxInput = kTurningEncoderPositionFactor  # radian

    kDrivingP = 0.04
    kDrivingI = 0
    kDrivingD = 0
    kDrivingFF = 1 / kDriveWheelFreeSpeedRps
    kDrivingMinOutput = -1
    kDrivingMaxOutput = 1

    kTurningP = 1
    kTurningI = 0
    kTurningD = 0
    kTurningFF = 0
    kTurningMinOutput = -1
    kTurningMaxOutput = 1

    kDrivingMotorIdleMode = CANSparkMax.IdleMode.kBrake
    kTurningMotorIdleMode = CANSparkMax.IdleMode.kBrake

    kDrivingMotorCurrentLimit = 50  # amp
    kTurningMotorCurrentLimit = 20  # amp


class OIConstants:
    kDriverControllerPort = 0
    kDriveDeadband = 0.05


class AutoConstants:
    kMaxSpeedMetersPerSecond = 3
    kMaxAccelerationMetersPerSecondSquared = 3
    kMaxAngularSpeedRadiansPerSecond = math.pi
    kMaxAngularSpeedRadiansPerSecondSquared = math.pi

    kPXController = 1
    kPYController = 1
    kPThetaController = 1

    # Constraint for the motion profiled robot angle controller
    kThetaControllerConstraints = TrapezoidProfileRadians.Constraints(
        kMaxAngularSpeedRadiansPerSecond, kMaxAngularSpeedRadiansPerSecondSquared
    )

class LiftConstants:
    motor_one = 9
    motor_two = 10

    max_speed_motor = .25

    # pls tune! :3 
    setpoint_store = 0.050
    setpoint_l1 = 0.050
    setpoint_l2 = 0.075
    setpoint_l3 = 0.155
    setpoint_l4 = 0.250
    setpoint_intake = 0.050 # UNTUNED
    setpoint_bludgeon_low = 0.050 # UNTUNED
    setpoint_bludgeon_high = 0.050 # UNTUNED

    P = 5
    I = 0
    D = 0
    # en.wikipedia.org/wiki/Iz*One
    i_zone = 0
    Ff = 0
    PIDEpsilon = 0.02

class JointConstants:
    motor = 11

    max_speed_motor = 0.2

    # TUNE OR ELSE!!!!!!!!!
    setpoint_store = 0.600
    setpoint_scorel4 = 0.330
    setpoint_scorel3 = 0.445
    setpoint_scorel2 = 0.390
    setpoint_intake = 0.330 # UNTUNED
    setpoint_intake2 = 0.330 # UNTUNED
    setpoint_bludgeon = 0.330 # UNTUNED

    P = 5
    I = 0
    D = 0
    i_zone = 0
    Ff = 0
    PIDEpsilon = 0.02

    bludgeon_speed = 0.05

class AlgaeConstants:
    motor_raise = 12
    motor_eat = 13

    max_speed_motor = 0.17

    # tuna or else...
    setpoint_up = 0.800
    setpoint_down = 0.950
    
    consumed_threshold = 0.260

    P = 5
    I = 0
    D = 0
    i_zone = 0
    Ff = 0

    intake_speed = -0.25
    outake_speed = 0.25
    stoptake_speed = 0

class GrabberConstants:
    motor = 14

    max_speed_motor = 0.2

    # tuna or else...
    setpoint_closed = 0
    setpoint_open = 0.2
    setpoint_intake = 0.2
    setpoint_intake2 = 0.2

    P = 5
    I = 0
    D = 0
    i_zone = 0
    Ff = 0
    PIDEpsilon = 0.02

    hold_speed = 0.6
    release_speed = -0.1
    stop_speed = 0.0
    
class RollerConstants:
    motor_id = 15

    intake_speed = -0.3
    outake_speed = 0.6
    stoptake_speed = 0

class HeatSeekingMissileLockheedMartinConstants:
    apriltag_position_threshold = 0.1