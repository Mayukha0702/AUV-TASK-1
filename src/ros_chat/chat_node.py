#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import threading

def callback(msg):
    if msg.data.startswith(username + ":"):
        return  # Skip printing own message
    print("\n" + msg.data + "\n> ", end='')

def publisher_loop(pub):
    while not rospy.is_shutdown():
        text = input("> ")
        message = f"{username}: {text}"
        pub.publish(message)

if __name__ == "__main__":
    rospy.init_node("chat_node", anonymous=True)
    username = input("Enter your name (e.g., Jolyne or Joestar): ")

    pub = rospy.Publisher("/chat_topic", String, queue_size=10)
    sub = rospy.Subscriber("/chat_topic", String, callback)

    threading.Thread(target=publisher_loop, args=(pub,)).start()
    rospy.spin()
