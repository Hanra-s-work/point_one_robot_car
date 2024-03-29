##
# EPITECH PROJECT, 2023
# point_one_robot_car
# File description:
# main.py
##

import sys
import src.constants as CONST
from tty_ov import TTY, ColouriseOutput, AskQuestion


class MainTTY:
    """ The main class of the program """

    def __init__(self, colourise_output: bool = True) -> None:
        super().__init__()
        self.err = CONST.ERR
        self.error = CONST.ERROR
        self.success = CONST.SUCCESS
        self.colours = CONST.COLOURS
        # finish the imports
        self.co = ColouriseOutput()
        self.aq = AskQuestion()
        self.tty = TTY(
            self.err,
            self.error,
            self.success,
            self.co,
            self.aq,
            CONST.COLOURS,
            colourise_output
        )
        self.tty.load_basics()

    def main(self) -> None:
        """ The main function of the program """
        status = self.tty.mainloop()
        self.tty.unload_basics()
        print()
        sys.exit(status)


def test_function() -> None:
    """ A test function """
    print("Test function")


def test_function2() -> str:
    """ A test function """
    return "Test function2"


def test_function3() -> str:
    """ A test function """
    return input("Test function3:")


def test_function4() -> None:
    """ A test function """
    print(f"You have entered: {input('Test function4:')}")


# if __name__ == "__main__":
#     COLOURISE_OUTPUT = True
#     if "-nc" in sys.argv or "--no-colour" in sys.argv:
#         COLOURISE_OUTPUT = False
#     main = MainTTY(COLOURISE_OUTPUT)
#     main.main()
