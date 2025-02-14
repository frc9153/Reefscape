#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import wpilib
from wpilib import SmartDashboard, SendableChooser

from robotcontainer import RobotContainer


class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self):
        # Instantiate our RobotContainer.  This will perform all our button bindings, and put our
        # autonomous chooser on the dashboard.
        self.container = RobotContainer()
        self.autonomousCommand = None

        self.auto_selector = SendableChooser()

        self.auto_selector.setDefaultOption("Do NOTHING!", self.container.do_nothing)

        self.auto_selector.addOption("Mobility", self.container.mobility)

        self.auto_selector.addOption("(Left) Reef; NO LIMELIGHT", self.container.left_reef_no_limelight)
        self.auto_selector.addOption("(Left) Reef; Trough; NO LIMELIGHT", self.container.left_reef_trough_no_limelight)
        self.auto_selector.addOption("(Left) Reef", self.container.left_reef)
        self.auto_selector.addOption("(Left) Reef; Trough", self.container.left_reef_trough)
        self.auto_selector.addOption("(Left) Reef; Left L4", self.container.left_reef_l4_left)
        self.auto_selector.addOption("(Left) Reef; Right L4", self.container.left_reef_l4_right)

        self.auto_selector.addOption("(Center) Reef; NO LIMELIGHT", self.container.center_reef_no_limelight)
        self.auto_selector.addOption("(Center) Reef; Trough; NO LIMELIGHT", self.container.center_reef_trough_no_limelight)
        self.auto_selector.addOption("(Center) Reef", self.container.center_reef)
        self.auto_selector.addOption("(Center) Reef; Trough", self.container.center_reef_trough)
        self.auto_selector.addOption("(Center) Reef; Left L4", self.container.center_reef_l4_left)
        self.auto_selector.addOption("(Center) Reef; Right L4", self.container.center_reef_l4_right)

        self.auto_selector.addOption("(Right) Reef; NO LIMELIGHT", self.container.right_reef_no_limelight)
        self.auto_selector.addOption("(Right) Reef; Trough; NO LIMELIGHT", self.container.right_reef_trough_no_limelight)
        self.auto_selector.addOption("(Right) Reef", self.container.right_reef)
        self.auto_selector.addOption("(Right) Reef; Trough", self.container.right_reef_trough)
        self.auto_selector.addOption("(Right) Reef; Left L4", self.container.right_reef_l4_left)
        self.auto_selector.addOption("(Right) Reef; Right L4", self.container.right_reef_l4_right)

    def autonomousInit(self) -> None:
        self.autonomousCommand = self.container.getAutonomousCommand()

        if self.autonomousCommand:
            self.autonomousCommand.schedule()

    def teleopInit(self) -> None:
        if self.autonomousCommand:
            self.autonomousCommand.cancel()

    def testInit(self) -> None:
        commands2.CommandScheduler.getInstance().cancelAll()


if __name__ == "__main__":
    wpilib.run(MyRobot)
