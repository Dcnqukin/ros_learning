#!/usr/bin/ python
import roslib;roslib.load_manifest('homerobot_teleop')
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class Teleop:
    def_init_(self):
    pub = rospy.Publisher('cmd_vel',Twist)
    rospy.init_node('homerobot_teleop')
    rate = rospy.Rate(rospy.get_param('~hz',1))
    self.cmd = None

    cmd = Twist()
    cmd.linear.x = 0.2
    cmd.linear.y = 0
    cmd.linear.z = 0
    cmd.angular.x = 0
    cmd.angular.y = 0
    cmd.angular.z = 0.5

    self.cmd = cmd
    while not rospy.is_shutdown():
        str = "hello world %s"%rospy.get_time()
        rospy.loginfo(str)
        pub.publish(self.cmd)
        rate.sleep()

if_name_=='_main_':Teleop()
