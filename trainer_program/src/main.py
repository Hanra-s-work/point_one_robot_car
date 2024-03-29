##
# EPITECH PROJECT, 2023
# point_one_robot_car
# File description:
# main.py
##

import os
from src.get_data import GetData
from src.output_processed_data import OutputProccessedData


class Main:
    """ The main class of the program """

    def __init__(self, data_path: str = "./data", output_path: str = "./out", error: int = 84, success: int = 0) -> None:
        super().__init__()
        self.error = error
        self.success = success
        self.loaded_images = {}
        self.data_path = data_path
        self.output_path = output_path
        self.get_data = GetData(self.data_path)
        self.output_processed_data = OutputProccessedData(
            self.loaded_images,
            self.output_path
        )

    def main(self) -> None:
        """ The main function of the program """
        self.loaded_images = self.get_data.main()
        self.output_processed_data.main()


if __name__ == "__main__":
    def check_paths(data_path: str, output_path: str) -> None:
        """ Check the paths """
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        if not os.path.exists(output_path):
            os.makedirs(output_path)

    ERROR = 84
    SUCCESS = 0
    DATA_PATH = "./data"
    OUTPUT_PATH = "./out"
    check_paths(DATA_PATH, OUTPUT_PATH)
    MI = Main(
        DATA_PATH,
        OUTPUT_PATH,
        ERROR,
        SUCCESS
    )
    MI.main()
