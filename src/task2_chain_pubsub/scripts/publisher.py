#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def main():
    rospy.init_node("publisher_node")
    pub = rospy.Publisher("/multiples_of_2", Int32, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    n = 1
    while not rospy.is_shutdown():
        value = 2 * n
        rospy.loginfo(f"Publishing: {value}")
        pub.publish(value)
        n += 1
        rate.sleep()

if __name__ == "__main__":
    main()
