#!/usr/bin/env python

import rospy
import pandas as pd
from sensor_msgs.msg import Joy
from rpiHAT import ServoNT
import time
from datetime import datetime

# setup csv
csv = {"speed":[],"direction":[],"time":[]}

# setup servos
s=ServoNT(channel=1, freq=94.5)
t=ServoNT(channel=2, freq=94.5)

def callback(data):
    # log entire thing heard
    rospy.loginfo(rospy.get_caller_id() + ' I heard %s', data.axes)
    
    # duty cycle in range [0.10, 0.20]
    # scale steering value to dutycycle, then set and log it
    steer = (data.axes[0]*.05)+.15
    s.pulse(steer)
    rospy.loginfo(rospy.get_caller_id() + ' steering: %s, duty cycle %f', data.axes[0], steer)

    # scale throttle value to dutycycle, then set and log it
    throttle = (data.axes[4]*.05)+.15
    t.pulse(throttle)
    
    # create a csv file of the throttle and steering values versus time
    # untested btw
    csv["speed"].append(throttle)
    csv["direction"].append(steer)
    csv["time"].append(datetime.now)
    df = pd.DataFrame(csv)
    df.to_csv("out.csv", index=False)
    
    rospy.loginfo(rospy.get_caller_id() + ' throttle: %s, duty cycle %f', data.axes[1], throttle)

def listener():
    # start node and subscribe to joy
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('joy', Joy, callback)

    # zero servo positions
    s.pulse(0.15)
    t.pulse(0.15)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
