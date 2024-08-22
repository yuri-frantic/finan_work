#!/usr/bin/python3
##!/usr/bin/env/ python3				#interpreter pointer

import rospy					#import rospy library

from std_msgs.msg import String			#import class "String" - future messages type

if __name__ == '__main__':			#read more: https://pyneng.readthedocs.io/ru/latest/book/11_modules/if_name_main.html
	rospy.init_node('topic_gp')		#setup node name
	rospy.loginfo("Transmitter started")	#setup node start terminal message
	
	pub = rospy.Publisher("/our_transmitter", String, queue_size = 10)	#first - topic, second - messages type
										#queue_size - for assynch work of node
										#read more: http://wiki.ros.org/rospy/Overview/Publishers%20and%20Subscribers
	rate = rospy.Rate(2)				#setup rate 2Hz
	
	while not rospy.is_shutdown():						#while node not canceled
		msg = String()							#creating object msg of class String
		msg.data = "Hi, this is GamePad"					#"data" attribute setup
		pub.publish(msg)						#publishing "data" of "msg" to topic
		rate.sleep()							#delay 0.5sec

	rospy.loginfo("Transmitter was stopped")	#setup node stop terminal message
