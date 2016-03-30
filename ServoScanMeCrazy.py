#MongoDB Me Crazy - Chart out Robot Patrol

from pymongo import MongoClient
import pymongo
import json
import math
import matplotlib.pyplot as plt
import numpy as np
import logging
#  db.robot.find({},{run_number:1})
# -- ------------------------
# Initialize
logging.basicConfig(level=logging.INFO)
graphX = []
graphY = []
x_adjustment=0
y_adjustment=0
run_number = 20160324011612
robot_x = 0
robot_y = 0
client = MongoClient()
db = client.kirk
# -- ------------------------

x = []
y = []

#Find Last Robot Run
cursor = db.robot.find(
        {"run_number": run_number}
        ).sort([
        ("decision", pymongo.ASCENDING)])

logging.info(run_number)
for document in cursor:
    
     m_distance = document['distance']
     m_run_number = document['run_number']
     m_angle = float(document['angle'])
     m_robot= document['robot_id']
     m_distance_list = document['distance_list']
     m_decision = document['decision']
    
     grid_size=51
     #Pull Angles & Distances
     i=0
     for a_ang, a_dist in m_distance_list.iteritems():
          #Print the values in a grid of 51x51 on the terminal
          #Convert the distance and angle to (x,y) coordinates and scale it down
          x[i]=(int(a_dist*math.cos(math.pi*(a_ang)/180))/10)
          y[i]=(int(a_dist*math.sin(math.pi*(a_ang)/180))/10)

          #Rotate the readings so that it is printed in the correct manner
          for i in range(num_of_readings+1):	
               x[i]=(grid_size/2)-x[i]
		       y[i]=(grid_size/2)-y[i]

	      #Create a grid
	      grid = [[0 for a in xrange(grid_size)] for a in xrange(grid_size)] 
          
          
          for i in range (num_of_readings+1):
		if dist_l[i]<>lim:
			grid[y[i]][x[i]]=1	
	fence='-'*(grid_size+1)
	
	#Print the map
	print "Map:"
	print fence*2
	for i in range(grid_size/2):
		print "|",
		for j in range (grid_size):
			if (j==grid_size/2)and i==(grid_size/2)-1:
				print 'x',
			elif grid[i][j]==0:
				print ' ',
			else:
				print 'o',
		print "|"
	print fence*2
        
        
        
        #Calculate XYs
        myX = round((float(a_dist)*math.cos((float(a_ang)*math.pi/180))))
        myY = round((float(a_dist)*math.sin((float(a_ang)*math.pi/180))))
        
        graphX.append(myX)
        graphY.append(myY)
        
        
plt.plot(graphX,graphY,'x')
plt.show()
     #graphX = []
     #graphY = []

