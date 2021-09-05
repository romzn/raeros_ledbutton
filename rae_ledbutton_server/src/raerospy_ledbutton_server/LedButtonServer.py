#! /usr/bin/env python3

import rospy

from raepy import LedButton

from rae_ledbutton_messages.msg import button
from rae_ledbutton_messages.srv import led,blink,heartbeat

class LedButtonServer(object):
    def __init__(self,ns="",ledpin=15,buttonpin=13):
        self.__lb = LedButton(ledpin=ledpin,buttonpin=buttonpin)
        
        rospy.Service("~Led{}".format(ns), led, self.__handle_led_request)
        rospy.loginfo("%s: initialized" % "~Led{}".format(ns))

        rospy.Service("~Blink{}".format(ns), blink, self.__handle_blink_request)
        rospy.loginfo("%s: initialized" % "~Blink{}".format(ns))

        rospy.Service("~Heartbeat{}".format(ns), heartbeat, self.__handle_heartbeat_request)
        rospy.loginfo("%s: initialized" % "~Heartbeat{}".format(ns))

        self.__lb.button.register_rising_edge_cb(self.__button_pressed_handler)
        self.__lb.button.register_falling_edge_cb(self.__button_released_handler)

        self.__statepublisher = rospy.Publisher('~Button{}'.format(ns), button, queue_size=10)
        self.__statepublisher.publish("OFF")




    def __handle_led_request(self,request):
        if request.cmd.upper() == "ON":
            self.___lb.led.on(request.intensity)
        elif request.cmd.upper() == "OFF":
            self.__lb.led.off()
        return True
    
    def __handle_blink_request(self,request):
        self.__lb.led.blink(freq=request.freq,cnt=request.cnt)
        return True

    def __handle_heartbeat_request(self,request):
        if request.cmd.upper() == "ON":   
            self.__lb.led.heartbeat_on(speed=request.speed)
        elif request.cmd.upper() == "OFF":
            self.__lb.led.heartbeat_off()
        return True
    
    def __button_pressed_handler(self):
        self.__statepublisher.publish("ON")

    def __button_released_handler(self):
        self.__statepublisher.publish("OFF")

    
        
