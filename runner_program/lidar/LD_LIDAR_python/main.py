import serial
from CalcLidarData import CalcLidarData
import matplotlib.pyplot as plt
import math
import time
import numpy as np



#### il reste à travailler sur la calibration et faire une version c++

## pour le c++ : https://github.com/ldrobotSensorTeam/ldlidar_sdk/blob/master/src


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='polar')
ax.set_title('lidar (exit: Key E)',fontsize=18)

plt.connect('key_press_event', lambda event: exit(1) if event.key == 'e' else None)

ser = serial.Serial(port='COM6',
                    baudrate=230400,
                    timeout=5.0,
                    bytesize=8,
                    parity='N',
                    stopbits=1)

tmpString = ""
angles = list()
distances = list()
prevLine = None
prevText = None
FPS = 0
flag2c = False

def the_callback(angles, distances,FPS):
    global prevLine
    global prevText
    if not prevLine is None:
        prevLine.remove()
        prevText.remove()
    #distances*10 pour l'avoir en mm
    line = ax.scatter([-angle for angle in angles], distances, c="pink", s=5)
    ax.set_theta_offset(math.pi / 2)
    FPS = int(FPS)
    str_FPS= f"{FPS}"
    text = plt.text(5, 0.5, str_FPS, fontsize=12, color='red', ha='center', va='center')
    
    plt.pause(0.01)
    
    prevLine = line
    prevText = text

while True:
    start_time = time.time() 
    all_b = ser.read_all()
    for b in all_b:
        tmpInt = int( b)
        b = bytes([b])
        if (tmpInt == 0x54):
            tmpString +=  b.hex()+" "
            flag2c = True
            continue
        
        elif(tmpInt == 0x2c and flag2c):
            tmpString += b.hex()
            if(not len(tmpString[0:-5].replace(' ','')) == 90 ):
                tmpString = ""
                loopFlag = False
                flag2c = False
                continue

            lidarData = CalcLidarData(tmpString[0:-5])
            angles.extend(lidarData.Angle_i)
            distances.extend(lidarData.Distance_i)
            if(len(angles) > 50*12):
                split = [i for i in range(len(angles)-1) if angles[i+1]< angles[i]]
                first = angles[:split[0]+1]
                angles = angles[split[0]+1:]
                firstDist = distances[:split[0]+1] #*10 # *10 to have it in mm
                distances = distances[split[0]+1:] #*10
                angles2 = np.array(angles)
                distances2 = np.array(distances) * 10
                angles2 = np.array(angles)
                first2 = np.array(first)
                firstDist2 = np.array(firstDist) * 10
                first2 =first2[firstDist2<600]
                firstDist2 =firstDist2[firstDist2<600]
                the_callback(first2, firstDist2, FPS)
            tmpString = ""
        else:
            tmpString += b.hex()+" "
        
        flag2c = False
    if (time.time() - start_time)>0:
        FPS = 1.0 / (time.time() - start_time)
    
ser.close()