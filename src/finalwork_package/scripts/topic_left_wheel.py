#!/usr/bin/env/ python3				#interpreter pointer

import rospy

if __name__ == '__main__':
	rospy.init_node('our_first_node')	#setup node name
	rospy.loginfo("Node started")		#setup node start terminal message
	rospy.sleep(3)				#delay for 3 sec
	rospy.loginfo("Node ends")		#setup node stop terminal message

