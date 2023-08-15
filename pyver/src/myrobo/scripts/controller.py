#i/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import getch
if __name__=='__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("Node has been started")

    pub= rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(40)
    while not rospy.is_shutdown():
        msg = Twist()

        l= getch.getche()
        
        if l=='d':
            msg.linear.x = 1
            msg.angular.z = 0
        elif l=='w':
            msg.linear.x = 0
            msg.angular.z = 1
        elif l=='a':
            msg.linear.x = -1
            msg.angular.z = 0
        elif l=='s':
            msg.linear.x = 0
            msg.angular.z = -1
        pub.publish(msg)
        rate.sleep()
    