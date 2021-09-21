from rae_ledbutton_messages.srv import blink, heartbeat, led
from rae_ledbutton_messages.msg import button

import rospy

class LedButtonClient(object):
    def __init__(self):
        rospy.Subscriber("/rae_ledbutton_server/Button", button, self.__read_button_cb)
        self.__button_state = "OFF"
        rospy.wait_for_service("/rae_ledbutton_server/Led")
        self.__led_serviceproxy = rospy.ServiceProxy("/rae_ledbutton_server/Led",led)
        rospy.wait_for_service("/rae_ledbutton_server/Heartbeat")
        self.__heartbeat_serviceproxy = rospy.ServiceProxy("/rae_ledbutton_server/Heartbeat",heartbeat)
        rospy.wait_for_service("/rae_ledbutton_server/Blink")
        self.__blink_serviceproxy = rospy.ServiceProxy("/rae_ledbutton_server/Blink",blink)
        rospy.init_node("LedButtonClient")

        self.__button_pressed_handler = None
        self.__button_released_handler = None



    def led_on(self,intensity=100):
        self.__led_serviceproxy(cmd="on",intensity=intensity)

    def led_off(self):
        self.__led_serviceproxy(cmd="off",intensity=100)

    def heartbeat_on(self,speed=50):
        self.__heartbeat_serviceproxy(cmd="on",speed=speed)

    def heartbeat_off(self):
        self.__heartbeat_serviceproxy(cmd="off")

    def blink(self,freq=7,cnt=7):
        self.__blink_serviceproxy(freq=freq,cnt=cnt)
    
    def blink_on(self,freq=7):
        self.__blink_serviceproxy(freq=freq,cnt=0)

    def blink_off(self):
        self.__blink_serviceproxy(freq=0,cnt=0)

    
    def stop_blink(self):
        self.blink(freq=0)

    def __read_button_cb(self,data):
        self.__button_state = data.state
        if self.__button_state == "ON" and self.__button_pressed_handler != None:
            self.__button_pressed_handler()
        if self.__button_state == "OFF" and self.__button_released_handler != None:
            self.__button_released_handler()
        
    def button_state(self):
        if self.__button_state == "ON":
            return 1
        else: 
            return 0
        
    def register_release_event(self,cb):
        self.__button_released_handler = cb

    def register_press_event(self,cb):
        self.__button_pressed_handler = cb
    
