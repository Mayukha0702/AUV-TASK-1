#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    multiplied = msg.data * 10
    rospy.loginfo(f"Received {msg.data}, multiplied to {multiplied}")
    pub.publish(multiplied)

def main():
    global pub
    rospy.init_node("multiply_by_10_node")
    pub = rospy.Publisher("/times_10", Int32, queue_size=10)
    rospy.Subscriber("/multiples_of_2", Int32, callback)
    rospy.spin()

if __name__ == "__main__":
    main()
