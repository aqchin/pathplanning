#!/usr/bin/env python

#robot.py implementation goes here
from astar import AStar
import rospy

from std_msgs.msg import *

class Robot():
    def __init__(self):
        rospy.init_node('Robot', anonymous=True)

        self.sim_pub = rospy.Publisher(
            "map_node/sim_complete",
            Bool,
            queue_size = 15
        )

        rospy.sleep(1)

        AStar()
        # MDP goes here

        rospy.sleep(1)
        self.sim_pub.publish(True)
        rospy.sleep(1)
        rospy.signal_shutdown("Done.")

if __name__ == '__main__':
    r = Robot()
