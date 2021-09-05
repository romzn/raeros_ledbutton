#! /usr/bin/env python3

import time
from raerospy_ledbutton_client import LedButtonClient
import rospy
lb = LedButtonClient()


if __name__ == "__main__":
             
    input(">>lb.led_on(intensity=10) (enter)")
    lb.led_on(intensity=10)
    input(">>lb.led_on(intensity=100) (enter)")
    lb.led_on(intensity=100)
    input(">>lb.led_off() (enter)")
    lb.led_off()
    input(">>lb.blink() (enter)")
    lb.blink()
    input(">>lb.blink(freq=12,cnt=10) (enter)")
    lb.blink(freq=12,cnt=10)
    input(">>lb.blink(freq=2,cnt=10) (enter)")
    lb.blink(freq=2,cnt=10)
    input(">>lb.blink_on(freq=3) (enter)")
    lb.blink_on(freq=3)
    input(">>lb.blink_off() (enter)")
    lb.blink_off()

    input(">>lb.heartbeat_on() (enter)")
    lb.heartbeat_on()
    input(">>lb.heartbeat_off() (enter)")
    lb.heartbeat_off()

    input(">>lb.heartbeat_on(speed=1)")
    lb.heartbeat_on(speed=1)
    input(">>lb.heartbeat_off()")
    lb.heartbeat_off()

    input(">>lb.heartbeat_on(speed=3)")
    lb.heartbeat_on(speed=3)
    input(">>lb.heartbeat_off()")
    lb.heartbeat_off()

    input(">>lb.button_state()")
    lb.button_state()

    print("Register function onpress()")
    input(">>lb.register_press_event(onpress)")
    
    def onpress():
        print("onpress:event")

    lb.register_press_event(onpress)

    print("Register function onpress()")
    input(">>lb.register_release_event(onpress)")

    def onrelease():
        print("release:event")

    lb.register_release_event(onrelease)




