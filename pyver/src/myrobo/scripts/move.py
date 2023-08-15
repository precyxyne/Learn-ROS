#i/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
def callback(msg):
    rospy.loginfo(msg)
if __name__=='__main__':
    rospy.init_node("move")
    rospy.loginfo("Node has been started")
    m=1/1.007999897
    n=1/1.0080000162124634
    pub= rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    pon= rospy.Subscriber("/turtle1/pose", Pose , callback)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        r=float(input())
        msg = Twist()
        msg.linear.x = r*m
        msg.angular.z = 0*n
        pub.publish(msg)
        rate.sleep()
        
    