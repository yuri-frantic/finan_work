#!/usr/bin/python3				#interpreter pointer
##!/usr/bin/env/ python3
import rospy					#import rospy library

if __name__ == '__main__':			#read more: https://pyneng.readthedocs.io/ru/latest/book/11_modules/if_name_main.html
	rospy.init_node('topic_rw')		#setup node name
	rospy.loginfo("Node started")		#setup node start terminal message
	rate = rospy.Rate(1)			#setup rate 10Hz
	while not rospy.is_shutdown():		#while node not canceled
		rospy.loginfo("Node runs")	#setup node stop terminal message
		rate.sleep()			#dealay 0.1sec
	rospy.loginfo("Node ends")		#setup node stop terminal message

