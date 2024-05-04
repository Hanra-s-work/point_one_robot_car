##
# EPITECH PROJECT, 2023
# point_one_robot_car
# File description:
# main.py
##

import sys
from colourise_output import ColouriseOutput
from motor_controller_api import MotorController
import spline as sp

CO = ColouriseOutput()


class Main:
    """ The main class of the program """

    def __init__(self, error: int = 1, success: int = 0, serial_port: str = "", co: ColouriseOutput = None, debug: bool = False) -> None:
        if debug is True:
            co.display("0B", (), "INFO:")
            co.display("0R", (), "Initialising the main class.\n")
        self.co = co
        self.error = error
        self.success = success
        self.debug = debug
        self.motor_controller = MotorController(
            serial_port,
            success,
            error,
            debug
        )
        self.sp = sp
        if debug is True:
            co.display("0B", (), "INFO:")
            co.display("0R", (), "Main class initialised\n")

    def _print_debug(self, string: str = "") -> None:
        if self.debug is True:
            print(f"(m) {string}", file=sys.stderr)

    def main(self) -> int:
        """ The main function of the program """
        return self.success


if __name__ == "__main__":
    CO.init_pallet()
    CO.display("0A", (), "Welcome to Runner program")
    MI = Main(error=1, success=0, co=CO, debug=False)
    status = MI.main()
    CO.unload_ressources()
    sys.exit(status)
