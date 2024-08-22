#!/usr/bin/python3
##!/usr/bin/env/ python3				#interpreter pointer

import rospy					#import rospy library

from std_msgs.msg import String			#import class "String" - future messages type

def callback_recieve_data(msg):
	rospy.loginfo("Message received (Raspberry Pi): ")
	rospy.loginfo(msg)


if __name__ == '__main__':				#read more: https://pyneng.readthedocs.io/ru/latest/book/11_modules/if_name_main.html
	rospy.init_node('topic_pb')			#setup node name
	rospy.loginfo("Receiver started")		#setup node start terminal message
	sub = rospy.Subscriber("/our_transmitter", String, callback_recieve_data)	#first - topic
							#second - messages type
							#third - call function
	rospy.spin()					#delay analog, but node do nothing until interrupt (only interrupt call function)
							#read more: https://answers.ros.org/question/332192/difference-between-rospyspin-and-rospysleep/

