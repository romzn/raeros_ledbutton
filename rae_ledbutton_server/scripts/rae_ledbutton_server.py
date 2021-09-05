#! /usr/bin/env python3

import rospy

from raerospy_ledbutton_server import LedButtonServer

if __name__ == "__main__":
    rospy.init_node('rae_ledbutton_server')
    perception_system = rospy.get_param('/rae/perception_system')
    if perception_system == "kinect":
        LedButtonServer(ns=1)
        LedButtonServer(ns=2, ledpin=16,buttonpin=18)

    else:
        LedButtonServer()

    rospy.spin()