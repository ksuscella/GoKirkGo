#!/usr/bin/env python
########################################################################                                                                  
# Test program to capture distances & experiment with grids
########################################################################
from gopigo import *

print "Press ENTER to start scan"
raw_input()				#Wait for input to start

mid_servo_pos=80 			# middle
start_servo_pos = 0			# start angle
end_servo_pos= 160 			# end angle - prevent servo damage
increm = 1 					# degree to increment
sample = 5 					# Lets capture more than one distance 
lim = 250					# max distance value

myX = []
myY = []

#Loop over angles and capture results
for a_ang in xrange(start_servo_pos,end_servo_pos+increm,increm):
	dist_l = []
	servo(a_ang)
	time.sleep(.25) # Give it time to get into position
	for a_sample in xrange(1,sample+1,1):
		dist_l.append(us_dist(15))
		time.sleep(.01)
	
	#Find the sample that is most common among all the samples for a particular angle
	dist=Counter(dist_l).most_common()	
	if dist > lim:	#max distance at 250cm
		dist = lim
	
	print("\""+str(a_ang)+"\":" + str(dist) + ",")
	
	