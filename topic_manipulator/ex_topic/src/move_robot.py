#! /usr/bin/env python

'''this is for python interface control'''

import rospy
from geometry_msgs.msg import Pose

rospy.init_node('move_robot_node')
pub = rospy.Publisher('/open_manipulator/input_kinematics_pose', Pose, queue_size = 1)
rate = rospy.Rate(2)
move = Pose()
move.orientation.w = 0
move.orientation.x = 0
move.orientation.y = 0
move.orientation.z = 1

move.position.x = 0.2
move.position.y = -0.2
move.position.z = 0.05

while not rospy.is_shutdown():
    pub.publish(move)
    rate.sleep()
