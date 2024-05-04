##
# EPITECH PROJECT, 2023
# point_one_robot_car
# File description:
# motor_controller_api.py
##

import sys
import time
from colourise_output import ColouriseOutput
from pyvesc import VESC

LEFT = 1
RIGHT = -1


class MotorController:
    """ The class in charge of controling the movements of the motor """

    def __init__(self, serial_port: str = "/dev/serial/by-id/usb-STMicroelectronics_ChibiOS_RT_Virtual_COM_Port_301-if00", success: int = 0, error: int = 84, debug: bool = False) -> None:
        # Motor management
        self.serial_port = serial_port
        self.motor = VESC(serial_port=serial_port)
        # Status codes
        self.error = error
        self.success = success
        # Command management
        self.command_delay = 0.01
        # Motor speed
        self.speed = 0
        self.running = False
        # Motor angle management
        self.angle = 0
        self.raw_angle = 0
        self.angle_max = 30
        self.angle_min = -30
        self.range_min = 0
        self.range_max = 100
        self.angle_middle = 0
        self.wheels_straight = True
        self.wheel_radius = 4  # cm
        # Debugging functions
        self.debug = debug
        # Adding colour to the mix
        self.co = ColouriseOutput()
        self.co.init_pallet()
        self.reset_colour = "\033[0m"
        self.info_colour = "\033[01;96m"
        self.error_colour = "\033[01;91m"

    def _print_debug(self, string: str) -> None:
        """ Function in charge of displaying the debug for the class """
        if self.debug is True:
            print(f"(mc) {string}", file=sys.stderr)

    def reload(self, serial_port="") -> int:
        """ A function to reload the controller """
        if serial_port != "":
            self.serial_port = serial_port
        self.motor = VESC(serial_port=serial_port)
        return self.success

    def _set_speed(self, speed: float) -> None:
        """ Set the speed of the motor """
        self.motor.set_duty_cycle(speed)

    def _smooth_it_out(self, old_speed: float, new_speed: float) -> None:
        """ Function in charge of slowing the movement """
        for i in range(old_speed, new_speed, -0.1):
            self._set_speed(i)
            time.sleep(self.command_delay)

    def _smooth_it_in(self, old_speed: float, new_speed: float) -> None:
        """ Function in charge of slowly speeding up the car """
        for i in range(old_speed, new_speed):
            self._set_speed(i)
            time.sleep(self.command_delay)

    def run(self, speed: int, smooth_out: bool = True, smooth_in: bool = False) -> bool:
        """ The function in charge of controling the speed of the car """
        if speed < 0:
            self._print_debug(
                f"{self.info_colour}INFO:{self.reset_colour} going into reverse"
            )
        else:
            self._print_debug(
                f"{self.info_colour}INFO:{self.reset_colour} going forward"
            )
        if speed > self.speed:
            if smooth_in is True:
                self._print_debug(
                    f"{self.info_colour}INFO:{self.reset_colour} smoothing in"
                )
                self._smooth_it_in(self.speed, speed)
            else:
                self._set_speed(speed)
            return True
        if smooth_out is True:
            self._print_debug(
                f"{self.info_colour}INFO: {self.reset_colour} smoothing out"
            )
            self._smooth_it_out(self.speed, speed)
        else:
            self._set_speed(speed)
        self.speed = speed
        self._print_debug(
            f"{self.info_colour}INFO:{self.reset_colour} speed is now set to {self.speed}"
        )
        return True

    def _turn_wheels(self, angle: float) -> bool:
        """ The function that does the calls to the motor in charge of turning the wheels """
        self.motor.set_servo(angle)
        self.motor.stop_heartbeat()

    def turn(self, angle: float) -> bool:
        """ The function in charge of changing """
        if angle < self.angle_min or angle > self.angle_max:
            print(
                f"{self.error_colour}ERROR:{self.reset_colour} Angle range must be between {self.angle_min} and {self.angle_max}"
            )
            return False
        if angle == 0:
            self._print_debug(
                f"{self.info_colour}INFO: {self.reset_colour} Wheels are now straight"
            )
            self.wheels_straight = True
            self.angle = 50
        else:
            self.wheels_straight = False
            self.angle = (
                (angle - self.angle_min) / (self.angle_max - self.angle_min)
            ) * (self.range_max - self.range_max) + self.range_min
        self._turn_wheels(self.angle)
        self.raw_angle = angle
        return True

    def is_running(self) -> bool:
        """ Check if the car is moving """
        return self.running

    def is_straight(self) -> bool:
        """ Check if the angle of the wheels is straight (that they are facing forward) """
        return self.wheels_straight

    def get_angle(self) -> float:
        """ Get the current angle of the wheels """
        return self.raw_angle

    def get_speed(self) -> float:
        """ Get the current speed of the car """
        return self.speed

    def abort_mission(self) -> bool:
        """ Function in charge of stopping the car completely (in case of an emergency) """
        self._print_debug(
            f"{self.info_colour}INFO: {self.reset_colour} Aborting mission"
        )
        if self.run(0, False, False) is not True or self.turn(0) is not True:
            return False
        return True
