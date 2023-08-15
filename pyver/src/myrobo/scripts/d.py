import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
class fossa:
     goop = 0
     mel=Pose()
     mel.x=5.544445
     mel.y=5.544445
     kil=Twist()

def xil(pol,pom:Pose):
    return ((pol.x-pom.x)**2+(pol.y-pom.y)**2)**0.5

def callback(msg:Pose):
    if msg.y-fossa.mel.y>=2 and (round(msg.theta,2)==round(0,2)) or (round(msg.x,1)>round(fossa.mel.x,1)):
        fossa.kil.angular.z = -1
        fossa.kil.linear.x = 1
        pub.publish(fossa.kil)
    elif round(msg.x,2)==round(fossa.mel.x,2) and round(msg.y,2)==round(fossa.mel.y,2) and (round(math.cos(msg.theta),3)==round(math.cos(math.pi/2),3)):
        fossa.kil.angular.z = 0
        fossa.kil.linear.x =1
        pub.publish(fossa.kil)
       
    elif round(msg.x,2)==round(fossa.mel.x,2) and round(msg.y,2)==round(fossa.mel.y,2):
        fossa.kil.angular.z = 0.1
        fossa.kil.linear.x =0
        pub.publish(fossa.kil)
        
    elif(msg.y-fossa.mel.y>=2) and (round(msg.theta,2)!=round(0,2)):
        fossa.kil.angular.z = -0.5
        fossa.kil.linear.x = 0
        pub.publish(fossa.kil)  
    elif round(msg.x,1)==round(fossa.mel.x,1) and round(math.cos(msg.theta),1)==round(math.cos(math.pi),1):
        fossa.kil.angular.z = 0
        fossa.kil.linear.x =0
        pub.publish(fossa.kil)
    elif (round(msg.x,1)==round(fossa.mel.x,1)):
        fossa.kil.angular.z = 0
        fossa.kil.linear.x =1
        pub.publish(fossa.kil)
    rospy.loginfo(msg)
    
if __name__=='__main__':
    rospy.init_node("draw_hex")
    rospy.loginfo("Node has been started")
    pub= rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    goop=0
    pon= rospy.Subscriber("/turtle1/pose", Pose , callback)
    rospy.spin()