##
# EPITECH PROJECT, 2023
# point_one_robot_car
# File description:
# motor_controller_api.py
##

import time
from pyvesc import VESC

LEFT = 1
RIGHT = -1


class MotorController:
    """ The class in charge of controling the movements of the motor """

    def __init__(self, serial_port: str = "/dev/serial/by-id/usb-STMicroelectronics_ChibiOS_RT_Virtual_COM_Port_301-if00", success: int = 0, error: int = 84) -> None:
        # Motor management
        self.serial_port = serial_port
        self.motor = VESC(serial_port=serial_port)
        # Status codes
        self.error = error
        self.success = success
        # Command managment
        self.command_delay = 0.01
        # Motor speed
        self.speed = 0
        self.running = False
        # Motor angle management
        self.angle = 0
        self.angle_max = 30
        self.angle_min = -30
        self.range_min = 0
        self.range_max = 100
        self.angle_middle = 0
        self.wheels_straight = True
        self.wheel_radius = 4  # cm

    def reload(self, serial_port="") -> int:
        """ A function to reload the controller """
        if serial_port != "":
            self.serial_port = serial_port
        self.motor = VESC(serial_port=serial_port)
        return self.success

    def _set_speed(self, speed: float) -> None:
        """ Set the speed of the motor """
        self.motor.set_duty_cycle(speed)

    def _smooth_it_out(self, old_speed: int, new_speed: int) -> None:
        """ Function in charge of slowing the movement """
        for i in range(old_speed, new_speed, -0.1):
            self._set_speed(i)
            time.sleep(self.command_delay)

    def run(self, speed: int, smooth_out: bool = True) -> bool:
        """ The function in charge of controling the speed of the car """
        if speed < 0:
            print("Speed cannot be negative")
            return False
        if speed > self.speed:
            self.speed = speed
            self._set_speed(speed)
            return True
        if smooth_out is True:
            self._smooth_it_out(self.speed, speed)
        else:
            self._set_speed(speed)
        self.speed = speed
        return True

    def _turn_wheels(self, angle: float) -> bool:
        """ The function that does the calls to the motor in charge of turning the wheels """
        self.motor.set_servo(angle)
        self.motor.stop_heartbeat()

    def turn(self, angle: float) -> bool:
        """ The function in charge of changing """
        if angle < self.angle_min or angle > self.angle_max:
            print(
                f"Angle range must be between {self.angle_min} and {self.angle_max}"
            )
            return False
        if angle == 0:
            self.wheels_straight = True
            self.angle = 50
        else:
            self.wheels_straight = False
            self.angle = (
                (angle - self.angle_min) / (self.angle_max - self.angle_min)
            ) * (self.range_max - self.range_max) + self.range_min
        self._turn_wheels(self.angle)
        return True
