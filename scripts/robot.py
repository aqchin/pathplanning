#!/usr/bin/env python

#robot.py implementation goes here
import astar, mdp
import rospy
from std_msgs.msg import Bool
from cse_190_assi_3.msg import AStarPath

class Robot():
    def __init__(self):
        rospy.init_node('Robot', anonymous=True)

        self.pl_pub = rospy.Publisher(
            "results/path_list",
            AStarPath,
            queue_size = 10
        )
        self.sim_pub = rospy.Publisher(
            "map_node/sim_complete",
            Bool,
            queue_size = 15
        )

        path_list = astar.astar()
        for pl in path_list:
            asp = AStarPath()
            asp.data = pl
            rospy.sleep(1)
            self.pl_pub.publish(asp)

        mdp.mdp()

        self.sim_pub.publish(True)
        rospy.sleep(1)
        rospy.signal_shutdown("Done.")

if __name__ == '__main__':
    try:
        Robot()
    except rospy.ROSInterruptException:
        pass
