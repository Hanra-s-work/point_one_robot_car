##
# EPITECH PROJECT, 2023
# point_one_robot_car
# File description:
# motor_controller_api.py
##

import serial


class MotorController:
    """ The class in charge of controling the movements of the motor """

    def __init__(self) -> None:
        self.speed = 0
        self.angle = 0
        self.angle_min = -30
        self.angle_max = 30
        self.angle_middle = 0
        self.running = False
        self.wheels_straight = True
        self.wheel_radius = 4  # cm

    def _smooth_it_out(self, old_speed: int, new_speed: int) -> None:
        """ Function in charge of slowing the movement """
        for i in range(old_speed, new_speed, -1):

    def run(self, speed: int) -> bool:
        """ The function in charge of controling the speed of the car """
        if speed >= 0:
            self.speed = speed
            # update the speed of the motor
            return True
        elif speed <= 1:
            self.speed = speed
            # update the speed of the motor
            return True

        print("Speed cannot be negative")
        return False

    def turn(self, angle: float) -> bool:
        """ The function in charge of changing """
        if (angle == 0):
            self.wheels_straight = True
            self.angle = 0
            # Update the angle of the wheels
