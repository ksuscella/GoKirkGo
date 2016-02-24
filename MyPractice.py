#!/usr/bin/env python
#############################################################################################################                                                                  

import os
import json
import math

import matplotlib.pyplot as plt
import numpy as np

print(os.getcwd())
os.chdir("/Users/kirk/Documents/GoPiGo/GoKirkGo/")
print(os.getcwd())
# Open a file
fo = open("distance.json", "r")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

parsed_json = json.loads(str(fo.read()))
fo.close()

#print(parsed_json['5'])

myX = []
myY = []

for ang_l in xrange(0,175,5):
#for ang_l in xrange(60,105,5):
    dist_l = parsed_json[str(ang_l)]
    myX.append(int(dist_l*math.cos(math.pi*(ang_l)/180)))
    myY.append(int(dist_l*math.sin(math.pi*(ang_l)/180)))
    #print(str(ang_l) + ", " + str(x) + ", "+str(y) + ", " + str(dist_l))

plt.plot(myX,myY)
plt.show()

#slope, intercept = np.polyfit(np.log(myX), np.log(myY), 1)
#print(slope)
#plt.loglog(myX, myY, 'x')
#plt.show()