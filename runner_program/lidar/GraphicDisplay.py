#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## point_one_robot_car
## File Description:
## Lidar graphic display
##
import matplotlib.pyplot as plt
from math import pi
from time import time
from Lidar import Lidar


class GraphicDisplay:
    def __init__(self):
        self.fig = plt.figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111, projection='polar')
        self.ax.set_title('lidar (exit: Key E)', fontsize=18)
        self.fps = 0.0
        self.start_time = time()
        self.prevLine = None
        self.prevText = None

    def __del__(self):
        plt.close(self.fig)

    def draw(self, lidar_data: list):
        if self.prevLine is not None:
            self.prevLine.remove()
            self.prevText.remove()
        # distances*10 pour l'avoir en mm
        line = self.ax.scatter([-angle for angle in angles], distances, c="pink", s=5)
        self.ax.set_theta_offset(pi / 2)
        self.fps = 1.0 / (time() - self.start_time)
        str_fps = f"{self.fps}"
        text = plt.text(5, 0.5, str_fps, fontsize=12, color='red', ha='center', va='center')

        plt.pause(0.01)

        prevLine = line
        prevText = text
