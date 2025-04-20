#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def callback(msg):
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(msg, desired_encoding='mono8')
    cv2.imshow("Edge Detected Image", frame)
    cv2.waitKey(1)

def main():
    rospy.init_node('edge_subscriber')
    rospy.Subscriber('/edge_image', Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
