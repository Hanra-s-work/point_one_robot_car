##
## EPITECH PROJECT, 2024
## robocar
## File description:
## spline
##

import numpy as np
from scipy.interpolate import CubicSpline
# import matplotlib.pyplot as plt
# import xalglib

def procedural():
    x_raw = [8500, # A
             5000, # B
             1500, # C
             650, # D
             500, # E
             500.1, # F
             650.1, # G
             1500.1, # H
             3400, # I
             4250, # J
             4400, # K
             4400.1, # L
             4250.1, # M
             3400.1, # N
             2766.7, # O
             2133, # P
             1500.2, # Q
             650.2, # R
             500.2, # S
             500.3, # T
             650.3, # U
             1500.3, # V
             5000.1, # W
             6600.1, # X
             8500.1, # Y
             9350, # Z
             9500, # A2
             9500.1, # B2
             9350.1, # C2
             8500.2, # D2
             6600.2, # E2
             5750, # F2 
             5500, # G2
             5500.1, # H2
             5750.1, # I2
             6600.3, # J2
             7450, # K2
             7850, # L2
             8500.3, # M2
             9350.2, # N2
             9500.2, # O2
             9500.3, # P2
             9350.3] # Q2

    y_raw = [7000, # A
             7000, # B
             7000, # C
             6500, # D
             6000, # E
             5424.5, # F
             4849, # G
             4349, # H
             4349, # I
             3850, # J
             3424.5, # K
             2700, # L
             2075.5, # M
             1787.5, # N
             2075.5, # O
             2700, # P
             3062.25, # Q
             2700, # R
             2075.5, # S
             1500, # T
             1000, # U
             500, # V
             500, # W
             500, # X
             500, # Y
             1000, # Z
             1500, # A2
             2075.5, # B2
             2700, # C2
             3100, # D2
             3100, # E2
             3424.5, # F2
             4075.5, # G2
             4800, # H2
             5424.5, # I2
             5900, # J2
             5424.5, # K2
             4800, # L2
             4350, # M2
             4800, # N2
             5424.5, # O2
             6000, # P2
             6500] # Q2
    t = np.arange(len(x_raw))
    x_cubic = CubicSpline(t, x_raw)
    y_cubic = CubicSpline(t, y_raw)
    
    x_first_derivative = x_cubic(t, 1)
    x_second_derivative = x_cubic(t, 2)
    
    y_first_derivative = y_cubic(t, 1)
    y_second_derivative = y_cubic(t, 2)

    # plt.plot(x_raw, y_raw, 'o-', label='data')
    # plt.plot(x_first_derivative, y_first_derivative, label="S'")
    # plt.plot(x_second_derivative, y_second_derivative, label="S''")
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title('Interpolation Cubique et ses dérivées')
    # plt.legend()
    # plt.grid(True)
    # plt.show()

# if __name__ == "__main__":
#     procedural()
