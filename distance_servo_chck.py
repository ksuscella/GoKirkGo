#!/usr/bin/env python
########################################################################                                                                  
# Test program to capture distances & experiment with grids
########################################################################
from gopigo import *
from collections import Counter

import urllib
import urllib2

print "Press ENTER to start scan"
raw_input()				#Wait for input to start

mid_servo_pos=80 			# middle
start_servo_pos = 0			# start angle
end_servo_pos= 160 			# end angle - prevent servo damage
increm = 5 					# degree to increment
sample = 5 					# Lets capture more than one distance 
lim = 250					# max distance value

myX = []
myY = []

enable_servo()
json_string = "{"

#Loop over angles and capture results
for a_ang in xrange(start_servo_pos,end_servo_pos+increm,increm):
	dist_l = []
	servo(a_ang)
	avg_sum = 0
	time.sleep(.25) # Give it time to get into position
	for a_sample in xrange(1,sample+1,1):
		avg_sum = avg_sum + us_dist(15)
		dist_l.append(us_dist(15))
		time.sleep(.01)
	
	#Find the sample that is most common among all the samples for a particular angle
	#dist=Counter(dist_l).most_common()	
	dist = avg_sum/sample
	
	print("\""+str(a_ang)+"\":" + str(dist) + ",")
	json_string = json_string + "\""+str(a_ang)+"\":" + str(dist) + ","
disable_servo()

trim_length = len(json_string)-1	#trim comma out
json_string = json_string[:trim_length] + "}"
#Send findings to laptop
my_mac = '192.168.1.105'
url = 'http://' + my_mac + '/'

url = url + '?greeting='+json_string

req = urllib2.Request(url)
f = urllib2.urlopen(req)
response = f.read()
print(response)
f.close()