#i/usr/bin/env python3
import rospy
from std_msgs.msg import String
if __name__=='__main__':
    rospy.init_node("talk")
    rospy.loginfo("Node has been started")
    mub= rospy.Publisher("chatter", String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = input()
        mub.publish(msg)
        rate.sleep()
    