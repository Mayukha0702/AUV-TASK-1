#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    rospy.init_node('edge_publisher')
    pub = rospy.Publisher('/edge_image', Image, queue_size=10)
    bridge = CvBridge()
    cap = cv2.VideoCapture(0)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            continue
        edges = cv2.Canny(frame, 100, 200)
        edge_msg = bridge.cv2_to_imgmsg(edges, encoding='mono8')
        pub.publish(edge_msg)
        rate.sleep()

    cap.release()

if __name__ == "__main__":
    main()
