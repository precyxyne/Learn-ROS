import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
class fossa:
     goop = 0
     mel=Pose()
     mel.x=5.544445
     mel.y=5.544445
     r=0

def xil(pol,pom:Pose):
    return ((pol.x-pom.x)**2+(pol.y-pom.y)**2)**0.5
def callback(msg:Pose):
    kil=Twist()
    if(round(math.cos(msg.theta-fossa.goop),2)==round(math.cos(math.pi/3),2)):
            fossa.mel=msg
            fossa.goop= msg.theta

    if (xil(fossa.mel,msg)>=fossa.r):
        kil.linear.x=0
        kil.angular.z=0.5
        pub.publish(kil)
    else:
        kil.linear.x = 1
        kil.angular.z=0
        pub.publish(kil)
    rospy.loginfo(msg)

    
if __name__=='__main__':
    rospy.init_node("draw_hex")
    rospy.loginfo("Node has been started")
    fossa.r=int(input())
    pub= rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    pon= rospy.Subscriber("/turtle1/pose", Pose , callback)
    rate = rospy.Rate(1)
    rospy.spin()