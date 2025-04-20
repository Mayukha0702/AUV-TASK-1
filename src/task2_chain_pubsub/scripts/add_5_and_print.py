#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    final_result = msg.data + 5
    rospy.loginfo(f"Received {msg.data}, final result: {final_result}")

def main():
    rospy.init_node("add_5_node")
    rospy.Subscriber("/times_10", Int32, callback)
    rospy.spin()

if __name__ == "__main__":
    main()
