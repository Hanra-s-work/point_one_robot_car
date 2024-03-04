
from donkeycar.parts.controller import Joystick, JoystickController


class MyJoystick(Joystick):
    #An interface to a physical joystick available at /dev/input/js0
    def __init__(self, *args, **kwargs):
        super(MyJoystick, self).__init__(*args, **kwargs)

            
        self.button_names = {
            0x130 : 'A',
            0x131 : 'B',
            0x134 : 'Y',
            0x133 : 'X',
            0x137 : 'RB',
            0x136 : 'LB',
            0x13b : 'Start',
            0x13a : 'Back',
        }


        self.axis_names = {
            0x4 : 'RJUp',
            0x3 : 'RJLeft',
            0x11 : 'LJUp',
            0x10 : 'LJLeft',
        }



class MyJoystickController(JoystickController):
    #A Controller object that maps inputs to actions
    def __init__(self, *args, **kwargs):
        super(MyJoystickController, self).__init__(*args, **kwargs)


    def init_js(self):
        #attempt to init joystick
        try:
            self.js = MyJoystick(self.dev_fn)
            self.js.init()
        except FileNotFoundError:
            print(self.dev_fn, "not found.")
            self.js = None
        return self.js is not None


    def init_trigger_maps(self):
        #init set of mapping from buttons to function calls
            
        self.button_down_trigger_map = {
            'Start' : self.toggle_mode,
            'Y' : self.erase_last_N_records,
            'B' : self.emergency_stop,
        }


        self.axis_trigger_map = {
            'LJLeft' : self.set_steering,
            'RJUp' : self.set_throttle,
        }


