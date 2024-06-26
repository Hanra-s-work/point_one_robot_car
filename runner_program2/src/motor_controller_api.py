##
# EPITECH PROJECT, 2023
# point_one_robot_car
# File description:
# motor_controller_api.py
##

import sys
import time
from colourise_output import ColouriseOutput
from pyvesc.VESC import VESC

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
        self.range_max = 1
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
        # Initialising the controller so that functions can be run
        time.sleep(0.5)
        self.run(0, False, False)

    def _print_debug(self, string: str) -> None:
        """ Function in charge of displaying the debug for the class """
        if self.debug is True:
            print(f"(mc) {string}", file=sys.stderr)

    def reload(self, serial_port="") -> int:
        """ A function to reload the controller """
        if serial_port != "":
            self.serial_port = serial_port
        self.motor = VESC(serial_port=serial_port)
        time.sleep(0.5)
        self.run(0, False, False)
        return self.success

    def _set_speed(self, speed: float) -> None:
        """ Set the speed of the motor """
        if (speed == 0):
            self.motor.set_rpm(0)
        else:
            self.motor.set_duty_cycle(speed)
        time.sleep(self.command_delay)

    def _smooth_it_out(self, old_speed: float, new_speed: float) -> None:
        """ Function in charge of slowing the movement """
        i = new_speed
        while i > old_speed:
            self._print_debug(
                f"{self.info_colour}INFO:{self.reset_colour} i = {i}"
            )
            self._set_speed(i)
            time.sleep(self.command_delay)
            i -= 0.01

    def _smooth_it_in(self, old_speed: float, new_speed: float) -> None:
        """ Function in charge of slowly speeding up the car """
        i = new_speed
        while i > old_speed:
            self._print_debug(
                f"{self.info_colour}INFO:{self.reset_colour} i = {i}"
            )
            self._set_speed(i)
            time.sleep(self.command_delay)
            i += 0.01

    def run(self, speed: float = 0.02, smooth_out: bool = True, smooth_in: bool = False) -> bool:
        """
          The function in charge of controling the speed of the car 
          The maximum value is 0.1 (move forward)
          The minimum value is -0.1 (move backwards)
          The center value is 0 (Stop position move)
          The step to be used is 0.01
        """
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
        self._print_debug(
            f"{self.info_colour}INFO:{self.reset_colour} angle = {angle}"
        )
        self.motor.set_servo(angle)
        time.sleep(self.command_delay)

    def turn(self, angle: float) -> bool:
        """ 
        The function in charge of changing the angle of the wheels
        The minimum value is -24
        The maximum value is 30
        The center value is 0
        The Step is 0.1 or 1.0
        **PS:** 
           * The operation in use is angle_to_be_applied = (your_angle + 30)/60
           * The result must not be in the 0.01 because the program only listens to 0.1 to 0.9 (0 means, full right, 1 means full left)
        """

        angle = float(angle)
        self._print_debug(
            f"{self.info_colour}INFO:{self.reset_colour} raw_angle = {angle}"
        )
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
            self.angle = 0.5
        else:
            self.wheels_straight = False
            self.angle = (angle+self.angle_max)/60.0
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

    def stop_car(self) -> bool:
        """ 
        Stop the infinite loop of the controller 
        But, you can start it again by using the reload function
        """
        self.motor.stop_heartbeat()
        return True

    def abort_mission(self) -> bool:
        """ Function in charge of stopping the car completely (in case of an emergency) """
        self._print_debug(
            f"{self.info_colour}INFO: {self.reset_colour} Aborting mission"
        )
        if self.run(0, False, False) is not True or self.turn(0) is not True:
            return False
        return self.stop_car()

    def emergency_stop(self) -> bool:
        """ Function in charge of stopping the car completely (in case of an emergency) """
        return self.abort_mission()


if __name__ == "__main__":
    CO = ColouriseOutput()
    CO.init_pallet()
    MI = MotorController(
        "COM15",
        success=0,
        error=0,
        debug=False
    )
    MI.run(0.02, False, False)  # Move forward full speed
    time.sleep(0.1)
    # # Get the firmware version
    # # print("Firmware: ", MI.motor.get_firmware_version())
    time.sleep(0.1)
    # # print(f"measurements = {dir(MI.motor.get_measurements())}")
    time.sleep(5)
    MI.run(0, False, False)  # Stop the car
    time.sleep(0.5)
    MI.run(-0.02, False, False)  # Move backward full speed
    time.sleep(5)
    MI.run(0, False, False)  # Stop the car
    print("Bla Bla")
    i = -30
    while i < 30:
        MI.turn(i)  # Turn the wheels
        time.sleep(0.5)
        i += 1
    print("Turning the other way")
    i = 30
    while i > -30:
        MI.turn(i)  # Turn the wheels
        time.sleep(0.5)
        i -= 1
    print("Resetting")
    MI.turn(0)  # Set the angle to the center
    MI.stop_car()  # Stop the controller
    CO.unload_ressources()
