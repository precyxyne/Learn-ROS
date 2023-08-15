#i/usr/bin/env python3
import rospy
from std_msgs.msg import String
def callback(msg):
    rospy.loginfo(msg)
if __name__=='__main__':
    rospy.init_node("listen")
    rospy.loginfo("Node has been started")
    mub= rospy.Subscriber("chatter", String, callback)
    rospy.spin()
    