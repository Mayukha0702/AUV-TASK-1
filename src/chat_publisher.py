#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def chat_publisher():
    rospy.init_node('chat_publisher', anonymous=True)
    pub = rospy.Publisher('chat_topic', String, queue_size=10)

    user = rospy.get_param('~user', 'Jolyne')  # Default to Jolyne if not specified

    rate = rospy.Rate(1)  # 1hz
    while not rospy.is_shutdown():
        message = input(f"{user}, enter your message: ")
        pub.publish(f"{user}: {message}")
        rate.sleep()

if __name__ == '__main__':
    try:
        chat_publisher()
    except rospy.ROSInterruptException:
        pass



