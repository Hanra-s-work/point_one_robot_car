##
# EPITECH PROJECT, 2023
# point_one_robot_car
# File description:
# output_processed_data.py
##

from PIL import Image


class OutputProccessedData:
    """ The class in charge of outputing the processed data """

    def __init__(self, data: dict[str, Image], output_path: str = "./out") -> None:
        self.data = data
        self.output_path = output_path

    def _save_images(self) -> None:
        """ Save the images """
        for image_name, image in self.data.items():
            image.save(f"{self.output_path}/{image_name}")

    def main(self) -> None:
        """ The main function of the class """
        self._save_images()
