#i/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
class fossa:
    mel=Pose()
def callback(msg):
    fossa.mel=msg
if __name__=='__main__':
    rospy.init_node("go_to_goal")
    rospy.loginfo("Node has been started")
    m=1/1.007999897
    n=1/(1.0080000162124634)

    pub= rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    pon= rospy.Subscriber("/turtle1/pose", Pose , callback)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        x=float(input())
        y=float(input())
        x=x-fossa.mel.x
        y=y-fossa.mel.y
        r=math.sqrt(x**2+y**2)
        q=math.acos(x/r)
        if y<0:
            q=-q
        q=q-fossa.mel.theta
        msg = Twist()
        msg.angular.z = q*n
        msg.linear.x = 0
        pub.publish(msg)
        time.sleep(2)
        msg.linear.x = r*m
        msg.angular.z = 0
        pub.publish(msg)
        rate.sleep()
        