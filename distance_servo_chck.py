#!/usr/bin/env python
########################################################################                                                                  
#
########################################################################
from gopigo import *

servo_pos=90
print "Press ENTER to start scan"
raw_input()				#Wait for input to start

# Ok Lets Start - reset position & capture distance
servo(servo_pos)
dist=us_dist(15)			#Find the distance of the object in front
print "Servo @: ",servo_pos," Distance: ",dist," cm"
time.sleep(.1)			# Take a break in between operations. 

servo_pos = 50 				# Prevent camera installation issues

while True:
	#Start Left to Right
	servo(servo_pos)
	dist=us_dist(15)
	print "Servo @: ",servo_pos," Distance: ",dist," cm"
	servo_pos=servo_pos+20
	time.sleep(.1)		# Take a break in between operations. 
	if servo_pos>130:
		break	
	
	 
	