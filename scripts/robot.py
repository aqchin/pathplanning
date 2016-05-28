#!/usr/bin/env python

#robot.py implementation goes here
import astar
from mdp import mdp
import rospy
from std_msgs.msg import Bool
from cse_190_assi_3.msg import AStarPath, PolicyList

class Robot():
    def __init__(self):
        rospy.init_node('Robot', anonymous=True)

        self.path_pub = rospy.Publisher(
            "results/path_list",
            AStarPath,
            queue_size = 10
        )
        self.policy_pub = rospy.Publisher(
            "results/policy_list",
            PolicyList,
            queue_size = 10
        )
        self.sim_pub = rospy.Publisher(
            "map_node/sim_complete",
            Bool,
            queue_size = 10
        )

        path_list = astar.astar()
        for pl in path_list:
            asp = AStarPath()
            asp.data = pl
            rospy.sleep(1)
            self.path_pub.publish(asp)

        markov = mdp()
        pl = PolicyList()
        pl.data = markov.policy_list
        rospy.sleep(1)


        rospy.sleep(1)
        rospy.sleep(1)
        self.policy_pub.publish(pl)
        #print markov.policy_list
        #for m in markov.policy_list:
            #pl = PolicyList()
            #pl.data = m
            #rospy.sleep(1)
            #self.policy_pub.publish(pl)

        self.sim_pub.publish(True)
        rospy.sleep(1)
        rospy.signal_shutdown("Done.")





if __name__ == '__main__':
    try:
        Robot()
    except rospy.ROSInterruptException:
        pass
