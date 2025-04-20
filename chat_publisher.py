#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def chat_callback(message):
    rospy.loginfo(rospy.get_caller_id() + " heard %s", message.data)

def chat_subscriber():
    rospy.init_node('chat_subscriber', anonymous=True)
    rospy.Subscriber('chat_topic', String, chat_callback)
    rospy.spin()

if __name__ == '__main__':
    chat_subscriber()
