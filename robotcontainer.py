import math

import commands2
import wpimath
import wpilib

from commands2 import cmd
from wpimath.controller import PIDController, ProfiledPIDControllerRadians
from wpimath.geometry import Pose2d, Rotation2d, Translation2d
from wpimath.trajectory import TrajectoryConfig, TrajectoryGenerator

from constants import AutoConstants, DriveConstants, LiftConstants, OIConstants, JointConstants, AlgaeConstants, GrabberConstants, RollerConstants
from subsystems.drivesubsystem import DriveSubsystem
from subsystems.liftsubsytem import LiftSubsystem
# from subsystems.algaesubsystem import AlgaeSubsystem
from subsystems.jointsubsystem import JointSubsystem
from subsystems.grabbersubsystem import GrabberSubsystem
from subsystems.rollersubsystem import RollerSubsystem
from commands.wowimfull import WowImFull
from commands.reefscorel4 import ReefScoreL4
from commands.reefscorel3 import ReefScoreL3
from commands.reefscorel2 import ReefScoreL2
from commands.lifttosetpoint import LiftToSetpoint
from commands.jointtosetpoint import JointToSetpoint


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        # The robot's subsystems
        # self.robotDrive = DriveSubsystem()
        self.robot_lift_please = LiftSubsystem()
        self.robot_joint_move = JointSubsystem()
        # self.robot_algae_score = AlgaeSubsystem()
        self.robot_grabber = GrabberSubsystem()
        self.robot_roller = RollerSubsystem()

        # self.lift_intake = commands2.cmd.runOnce(
        #     lambda: self.robot_lift_please.go_to_setpoint(
        #         LiftConstants.setpoint_intake
        #     ),
        #     self.robot_lift_please
        # )

        self.lift_store = commands2.cmd.runOnce(
            lambda: self.robot_lift_please.go_to_setpoint(
                LiftConstants.setpoint_store
            ),
            self.robot_lift_please
        )

        # self.lift_l1 = commands2.cmd.runOnce(
        #     lambda: self.robot_lift_please.go_to_setpoint(
        #         LiftConstants.setpoint_l1
        #     ),
        #     self.robot_lift_please
        # )

        # self.lift_l2 = commands2.cmd.runOnce(
        #     lambda: self.robot_lift_please.go_to_setpoint(
        #         LiftConstants.setpoint_l2
        #     ),
        #     self.robot_lift_please
        # )
        
        # self.lift_l3 = commands2.cmd.runOnce(
        #     lambda: self.robot_lift_please.go_to_setpoint(
        #         LiftConstants.setpoint_l3
        #     ),
        #     self.robot_lift_please
        # )

        # self.lift_l4 = commands2.cmd.runOnce(
        #     lambda: self.robot_lift_please.go_to_setpoint(
        #         LiftConstants.setpoint_l4
        #     ),
        #     self.robot_lift_please
        # )

        self.joint_intake = commands2.cmd.runOnce(
            lambda: self.robot_joint_move.go_to_setpoint(
                JointConstants.setpoint_intake
            ),
            self.robot_joint_move
        )

        self.joint_scorehigh = commands2.cmd.runOnce(
            lambda: self.robot_joint_move.go_to_setpoint(
                JointConstants.setpoint_scorel4
            ),
            self.robot_joint_move
        )

        self.joint_scoremid = commands2.cmd.runOnce(
            lambda: self.robot_joint_move.go_to_setpoint(
                JointConstants.setpoint_scorel3
            ),
            self.robot_joint_move
        )

        self.joint_scoretrough = commands2.cmd.runOnce(
            lambda: self.robot_joint_move.go_to_setpoint(
                JointConstants.setpoint_scorel2
            ),
            self.robot_joint_move
        )

        # self.algae_up = commands2.cmd.runOnce(
        #     lambda: self.robot_algae_score.go_to_setpoint(
        #         AlgaeConstants.setpoint_up
        #     ),
        #     self.robot_algae_score
        # )

        # self.algae_down = commands2.cmd.runOnce(
        #     lambda: self.robot_algae_score.go_to_setpoint(
        #         AlgaeConstants.setpoint_down
        #     ),
        #     self.robot_algae_score
        # )

        # self.algae_intake = commands2.cmd.runOnce(
        #     lambda: self.robot_algae_score.set_chomp_power(
        #         AlgaeConstants.intake_speed
        #     ),
        #     self.robot_algae_score
        # )

        # self.algae_outake = commands2.cmd.runOnce(
        #     lambda: self.robot_algae_score.set_chomp_power(
        #         AlgaeConstants.outake_speed
        #     ),
        #     self.robot_algae_score
        # )

        # self.algae_stoptake = commands2.cmd.runOnce(
        #     lambda: self.robot_algae_score.set_chomp_power(
        #         AlgaeConstants.stoptake_speed
        #     ),
        #     self.robot_algae_score
        # )

        self.grabber_grab = commands2.cmd.runOnce(
            lambda: self.robot_grabber.set_power(
                GrabberConstants.hold_speed
            ),
            self.robot_grabber
        )

        self.grabber_release = commands2.cmd.runOnce(
            lambda: self.robot_grabber.set_power(
                GrabberConstants.release_speed
            ),
            self.robot_grabber
        )

        self.grabber_stop = commands2.cmd.runOnce(
            lambda: self.robot_grabber.set_power(
                GrabberConstants.stop_speed
            ),
            self.robot_grabber
        )

        self.roller_grab = commands2.cmd.runOnce(
            lambda: self.robot_roller.set_power(
                RollerConstants.intake_speed
            ),
            self.robot_roller
        )

        self.roller_release = commands2.cmd.runOnce(
            lambda: self.robot_roller.set_power(
                RollerConstants.outake_speed
            ),
            self.robot_roller
        )

        self.roller_stop = commands2.cmd.runOnce(
            lambda: self.robot_roller.set_power(
                RollerConstants.stoptake_speed
            ),
            self.robot_roller
        )

        self.grabber_full_release = self.grabber_release.andThen(commands2.WaitCommand(0.1)).andThen(self.grabber_stop)

        # The driver's controller
        self.driverController = commands2.button.CommandXboxController(OIConstants.kDriverControllerPort)

        # Configure the button bindings
        self.configureButtonBindings()

        # Configure default commands
        # self.robotDrive.setDefaultCommand(
        #     # The left stick controls translation of the robot.
        #     # Turning is controlled by the X axis of the right stick.
        #     commands2.RunCommand(
        #         lambda: self.robotDrive.drive(
        #             -wpimath.applyDeadband(
        #                 self.driverController.getLeftY(), OIConstants.kDriveDeadband
        #             ),
        #             -wpimath.applyDeadband(
        #                 self.driverController.getLeftX(), OIConstants.kDriveDeadband
        #             ),
        #             -wpimath.applyDeadband(
        #                 self.driverController.getRightX(), OIConstants.kDriveDeadband
        #             ),
        #             True,
        #             True,
        #         ),
        #         self.robotDrive,
        #     )
        # )

    def configureButtonBindings(self) -> None:
        """
        Use this method to define your button->command mappings. Buttons can be created by
        instantiating a :GenericHID or one of its subclasses (Joystick or XboxController),
        and then passing it to a JoystickButton.
        """

        # # Run default command on the lift_intake subsystem. This will basically run it over
        # # and over until something else runs on lift_intake.
        # self.robot_lift_please.setDefaultCommand(
        #     # RunCommand is a function that turns a function into a Command. Good for less complicated stuff.
        #     commands2.RunCommand(
        #         # You need to pass a function to this. You can't pass parameters to a function normally,
        #         # and we need to pass getLeftY(), so we make a lambda around it. Basically we're constantly
        #         # setting the intake power to the left joystick's Y value.
        #         lambda: self.robot_lift_please.set_motor_power(self.driverController.getLeftY()),
        #         self.robot_lift_please
        #     )
        # )

        # self.robot_joint_move.setDefaultCommand(
        #     commands2.RunCommand(
        #         lambda: self.robot_joint_move.set_motor_power(self.driverController.getRightY()),
        #         self.robot_joint_move
        #     )
        # )
        
        # One time action--much simpler.
        # replace Y with the button you want. the thing passed to onTrue is a Command.
        self.driverController.a().onTrue(self.lift_store)
        self.driverController.b().onTrue(ReefScoreL2(self.robot_lift_please, self.robot_joint_move, self.robot_grabber))
        self.driverController.x().onTrue(ReefScoreL3(self.robot_lift_please, self.robot_joint_move, self.robot_grabber))
        self.driverController.y().onTrue(ReefScoreL4(self.robot_lift_please, self.robot_joint_move, self.robot_grabber))

        # self.driverController.a().onTrue(self.algae_down)
        # self.driverController.b().onTrue(self.algae_up)
        # self.driverController.x().onTrue(self.algae_outake)
        # self.driverController.x().onFalse(self.algae_stoptake)
        # self.driverController.y().whileTrue(WowImFull(self.robot_algae_score))

        self.driverController.leftBumper().onTrue(self.joint_intake)
        self.driverController.rightBumper().onTrue(self.joint_scorehigh)
        self.driverController.leftTrigger().onTrue(self.grabber_grab)
        self.driverController.rightTrigger().onTrue(self.grabber_full_release)
        
        # self.driverController.a().onTrue(self.roller_grab)
        # self.driverController.a().onFalse(self.roller_stop)
        # self.driverController.b().onTrue(self.roller_release)
        # self.driverController.b().onFalse(self.roller_stop)

        # reset_gyro = commands2.RunCommand(
        #     lambda: self.robotDrive.gyro.reset(),
        #     self.robotDrive
        # )

        # self.driverController.pov(90).onTrue(reset_gyro)

    def disablePIDSubsystems(self) -> None:
        """Disables all ProfiledPIDSubsystem and PIDSubsystem instances.
        This should be called on robot disable to prevent integral windup."""

    def getAutonomousCommand(self) -> commands2.Command:
        """Use this to pass the autonomous command to the main {@link Robot} class.

        :returns: the command to run in autonomous
        """
        # Create config for trajectory
        config = TrajectoryConfig(
            AutoConstants.kMaxSpeedMetersPerSecond,
            AutoConstants.kMaxAccelerationMetersPerSecondSquared,
        )
        # Add kinematics to ensure max speed is actually obeyed
        config.setKinematics(DriveConstants.kDriveKinematics)

        # An example trajectory to follow. All units in meters.
        exampleTrajectory = TrajectoryGenerator.generateTrajectory(
            # Start at the origin facing the +X direction
            Pose2d(0, 0, Rotation2d(0)),
            # Pass through these two interior waypoints, making an 's' curve path
            [Translation2d(1, 1), Translation2d(2, -1)],
            # End 3 meters straight ahead of where we started, facing forward
            Pose2d(3, 0, Rotation2d(0)),
            config,
        )

        thetaController = ProfiledPIDControllerRadians(
            AutoConstants.kPThetaController,
            0,
            0,
            AutoConstants.kThetaControllerConstraints,
        )
        thetaController.enableContinuousInput(-math.pi, math.pi)

        # swerveControllerCommand = commands2.SwerveControllerCommand(
        #     exampleTrajectory,
        #     self.robotDrive.getPose,  # Functional interface to feed supplier
        #     DriveConstants.kDriveKinematics,
        #     # Position controllers
        #     PIDController(AutoConstants.kPXController, 0, 0),
        #     PIDController(AutoConstants.kPYController, 0, 0),
        #     thetaController,
        #     self.robotDrive.setModuleStates,
        #     (self.robotDrive,),
        # )

        # Reset odometry to the starting pose of the trajectory.
        # self.robotDrive.resetOdometry(exampleTrajectory.initialPose())

        # Run path following command, then stop at the end.
        # return swerveControllerCommand.andThen(
        #     cmd.run(
        #         lambda: self.robotDrive.drive(0, 0, 0, False, False),
        #         self.robotDrive,
        #     )
        # )
