import time
# from pyvesc import VESC
from pyvesc import VESC
import sys
sys.path.append("C:/Users/NBizar OUARTI/Documents/VESC_motor/PyVESC/")
# sys.path.append(
# "C:/Users/Henry_PC/Documents/001_GitHub/Hanra-s-work/point_one_robot_car/wenv/Lib/site-packages/pyvesc")


# serial port that VESC is connected to. Something like "COM3" for windows and as below for linux/mac
serial_port = '/dev/serial/by-id/usb-STMicroelectronics_ChibiOS_RT_Virtual_COM_Port_301-if00'
serial_port = 'COM9'
# serial_port = 'COM15'

# a function to show how to use the class with a with-statement


def run_motor_using_with():
    with VESC(serial_port=serial_port) as motor:
        print("Firmware: ", motor.get_firmware_version())
        motor.set_duty_cycle(.02)

        # run motor and print out rpm for ~2 seconds
        for i in range(30):
            time.sleep(0.1)
            print(motor.get_measurements().rpm)
        motor.set_rpm(0)


# Nizar todo angle as an input:  relation between full angle 100 and the real angle
# https://servodatabase.com/servo/traxxas/2056
# 60 ° range
# 30 ° right = 100
#  0 ° center = 50
# 30 ° left  = 0
# a function to show how to use the class as a static object.
# angle -30 : 30
# commande : ((angle - input_min) / (input_max - input_min)) * (output_max - output_min) + output_min
def run_motor_as_object():
    motor = VESC(serial_port=serial_port)
    print("Firmware: ", motor.get_firmware_version())

    # sweep servo through full range
    for i in range(0, 100):
        # if i ==10:

        time.sleep(0.01)
        motor.set_servo(i/100)

    # IMPORTANT: YOU MUST STOP THE HEARTBEAT IF IT IS RUNNING BEFORE IT GOES OUT OF SCOPE. Otherwise, it will not
    #            clean-up properly.
        motor.stop_heartbeat()


def time_get_values():
    with VESC(serial_port=serial_port) as motor:
        start = time.time()
        motor.get_measurements()
        stop = time.time()
        print("Getting values takes ", stop-start, "seconds.")


if __name__ == '__main__':
    run_motor_using_with()
    # run_motor_as_object()
    # time_get_values()
