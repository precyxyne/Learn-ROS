#i/usr/bin/env python3
import rospy

if __name__ =='__main__':
    rospy.init_node("test_node")

    rospy.loginfo("this is the start")

    rate=rospy.Rate(15)

    while not rospy.is_shutdown():
        rospy.loginfo("freedom")
        rate.sleep()