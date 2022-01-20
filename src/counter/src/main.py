#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64
current_val: int = 1

def callback(data)->None:
    """programmer should fill this doc field and annotation"""
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    global current_val
    current_val = current_val + data.data


def listener()->None:
    """programmer should fill this doc field and annotation"""
    rospy.init_node('counter', anonymous=True)
    rospy.Subscriber("add", Int64, callback)


def talker()->None:
    """programmer should fill this doc field and annotation"""
    pub = rospy.Publisher('total', Int64, queue_size=10)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        rospy.loginfo(current_val)
        pub.publish(current_val)
        pub.publish()
        rate.sleep()


if __name__ == '__main__':
    listener()
    talker()