#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## point_one_robot_car
## File Description:
## Lidar location and trajectory correction
##
import numpy as np

from LoadConfig import LoadConfig
from Lidar import Lidar
from Const import CONFIG_FILE_PATH


class LidarLocation:
    def __init__(self):
        self.config = LoadConfig(CONFIG_FILE_PATH)
        self.car = [0, 0]
        self.car_angle = 0
        self.pos = []
        self.lidar = Lidar()

    @staticmethod
    def polar_to_cartesian(r, theta):
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        return x, y

    async def get_lidar_data(self):
        while True:
            self.pos = self._predict_car_position(20, 2, 45, 10, 1000)
            self.lidar.read_serial_data()
            cones = self._get_cone_from_lidar()
            self._verify_position(cones, 20)

    def _verify_position(self, cones, threshold):
        collisions = 0
        buf = []
        for cone in cones:
            for pos in self.pos:
                distance = np.sqrt((pos[0] - cone[0]) ** 2 + (pos[1] - cone[1]) ** 2)
                if distance < threshold:
                    collisions += 1
                    buf.append(distance)
        collisions_probability = collisions / (len(cones) + len(self.pos))
        if collisions_probability > 0.1:
            distance_mean = np.mean(buf)
            return distance_mean
        return 0

    def _get_cone_from_lidar(self):
        detect = []
        for angle, dist in self.lidar.Angle_i, self.lidar.Distance_i:
            tmp = angle - self.car_angle
            tmp = LidarLocation.polar_to_cartesian(dist, tmp)
            detect.append(tmp)
        return detect

    def _predict_car_position(self, speed, speed_std_dev, direction, direction_std_dev, sample):
        positions = []
        for _ in range(sample):
            speed_sample = np.random.normal(speed, speed_std_dev)
            direction_sample = np.random.normal(direction, direction_std_dev)

            x = self.car[0] + speed_sample * np.cos(np.deg2rad(direction_sample))
            y = self.car[1] + speed_sample * np.sin(np.deg2rad(direction_sample))

            positions.append((x, y))
        return positions
