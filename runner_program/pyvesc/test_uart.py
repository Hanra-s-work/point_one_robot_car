import serial

# Open the COM port (replace 'COM7' with the actual port name)
ser = serial.Serial('COM7')

# Read data (e.g., 10 characters)
data = ser.read(10)
print(data)
