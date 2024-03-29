##
# EPITECH PROJECT, 2023
# point_one_robot_car
# File description:
# get_data.py
##

import os
from PIL import Image


class GetData:
    """ The class in charge of loading the data """

    def __init__(self, input_path: str = "./data") -> None:
        self.input_path = input_path
        self.images = {}

    def _get_available_images(self) -> list:
        """ Get the available images """
        return os.listdir(self.input_path)

    def _load_the_images(self) -> None:
        """ Load the images """
        images = self._get_available_images()
        for image in images:
            self.images[image] = Image.open(f"{self.input_path}/{image}")

    def main(self) -> dict[str, Image]:
        """ The main function of the class """
        self._load_the_images()
        return self.images
