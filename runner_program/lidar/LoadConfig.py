#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## point_one_robot_car
## File Description:
## Load config from json
##
from json import load


class LoadConfig:
    def __init__(self, path_to_file: str):
        try:
            file = open(path_to_file, 'r')
            self.file_content = load(file)
        except FileNotFoundError:
            print(f'File {path_to_file} not found')
        self.map = []

    def get_config(self):
        for elem in self.file_content["lidar"]:
            if elem["exist"]:
                self.map.append(elem["pos"])
