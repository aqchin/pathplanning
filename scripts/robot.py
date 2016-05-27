#!/usr/bin/env python

#robot.py implementation goes here
from astar import AStar
import rospy
from std_msgs.msg import Bool

class Robot():
    def __init__(self):
        rospy.init_node('Robot', anonymous=True)

        self.sim_pub = rospy.Publisher(
            "map_node/sim_complete",
            Bool,
            queue_size = 15
        )

        AStar()
        # MDP goes here

        self.sim_pub.publish(True)
        rospy.sleep(1)
        rospy.signal_shutdown("Done.")

if __name__ == '__main__':
    try:
        Robot()
    except rospy.ROSInterruptException:
        pass
