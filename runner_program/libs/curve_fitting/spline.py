import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, BSpline
# from alglib import 

def procedural():    
    x_raw = [8500, # A
             5000, # B
             1500, # C
             650, # D
             500, # E
             500, # F
             650, # G
             1500, # H
             3400, # I
             4250, # J
             4400, # K
             4400, # L
             4250, # M
             3400, # N
             2766.7, # O
             2133, # P
             1500, # Q
             650, # R
             500, # S
             500, # T
             650, # U
             1500, # V
             5000, # W
             6600, # X
             8500, # Y
             9350, # Z
             9500, # A2
             9500, # B2
             9350, # C2
             8500, # D2
             6600, # E2
             5750, # F2 
             5500, # G2
             5500, # H2
             5750, # I2
             6600, # J2
             7450, # K2
             7850, # L2
             8500, # M2
             9350, # N2
             9500, # O2
             9500, # P2
             9350] # Q2

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

    sorted_indices = np.argsort(x_raw)
    x = np.array(x_raw)[sorted_indices]
    y = np.array(y_raw)[sorted_indices]

    # Construct splines with different values of s
    tck = splrep(x, y, s=0)
    # tck_s = splrep(x, y, s=len(x))

    # Use of plot
    xnew = np.arange(0, 9/4, 1/50) * np.pi
    xnew = np.linspace(min(x), max(x), 100) 
    plt.plot(xnew, np.sin(xnew), '-.')
    plt.plot(xnew, BSpline(*tck)(xnew), '-')
    # plt.plot(xnew, BSpline(*tck_s)(xnew), '-', label=f's={len(x)}')
    plt.plot(x, y, 'o')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    procedural()
