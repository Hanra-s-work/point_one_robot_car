#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## point_one_robot_car
## File Description:
## Lidar runtime use
##
import serial
import math
import time


class Lidar:
    def __init__(self):
        """
        Initialize the Lidar
        """
        try:
            self.serial = serial.Serial('COM6', 230400, timeout=5.0, bytesize=8,)
        except serial.SerialException:
            print("Serial port not available")
        self.start_time = time.time()
        self.FSA = 0.0
        self.LSA = 0.0
        self.CS = 0
        self.Speed = 0
        self.TimeStamp = 0

        self.Confidence_i = []
        self.Angle_i = []
        self.Distance_i = []

    def __del__(self):
        """
        Lidar Destructor
        """
        self.serial.close()

    def _calc_lidar_data(self, string: str):
        """
        Parse data string, calculate Lidar data and update Lidar data.
        :param string:
        Args:
            string: str

        Returns:

        """
        string = string.replace(' ', '')

        speed = int(string[2:4] + string[0:2], 16) / 100
        fsa = float(int(string[6:8] + string[4:6], 16)) / 100
        lsa = float(int(string[-8:-6] + string[-10:-8], 16)) / 100
        time_stamp = int(string[-4:-2] + string[-6:-4], 16)
        cs = int(string[-2:], 16)

        confidence_i = list()
        angle_i = list()
        distance_i = list()
        if lsa - fsa > 0:
            angle_step = float(lsa - fsa) / 12
        else:
            angle_step = float((lsa + 360) - fsa) / 12

        counter = 0
        circle = lambda deg: deg - 360 if deg >= 360 else deg
        for i in range(0, 6 * 12, 6):
            distance_i.append(int(string[8 + i + 2:8 + i + 4] + string[8 + i:8 + i + 2], 16) / 100)
            confidence_i.append(int(string[8 + i + 4:8 + i + 6], 16))
            angle_i.append(circle(angle_step * counter + fsa) * math.pi / 180.0)
            counter += 1
        self.__update_lidar_data(fsa, lsa, time_stamp, cs, speed, confidence_i, angle_i, distance_i)

    def __update_lidar_data(self, fsa, lsa, cs, speed, time_stamp, confidence_i, angle_i, distance_i):
        """
        update lidar data on tick
        Args:
            fsa:
            lsa:
            cs:
            speed:
            time_stamp:
            confidence_i:
            angle_i:
            distance_i:

        Returns:
            None
        """
        self.FSA = fsa
        self.LSA = lsa
        self.CS = cs
        self.Speed = speed
        self.TimeStamp = time_stamp
        self.Confidence_i = confidence_i
        self.Angle_i = angle_i
        self.Distance_i = distance_i

    def read_serial_data(self):
        tmp_string = ""
        flag2c = False
        serial_data = self.serial.read_all()
        for elem in serial_data:
            tmp_int = int(elem)
            byte = bytes([elem])
            if tmp_int == 0x54:
                tmp_string += byte.hex() + " "
                flag2c = True
                continue

            elif tmp_int == 0x2c and flag2c:
                tmp_string += byte.hex()
                if not len(tmp_string[0:-5].replace(' ', '')) == 90:
                    tmp_string = ""
                    continue

                self._calc_lidar_data(tmp_string[0:-5])
                tmp_string = ""
            else:
                tmp_string += byte.hex() + " "
            flag2c = False
