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
run_number = 20160330013254
robot_x = 0
robot_y = 0
client = MongoClient()
db = client.kirk
# -- ------------------------

#Find Last Robot Run
cursor = db.robot.find(
        {"run_number": run_number}
        ).sort([
        ("decision", pymongo.ASCENDING)])

logging.info(run_number)
#logging.info("coords: " + str(robot_x) + ", " + str(robot_y))
# Loop over documents - calculate path & surrounding area   
for document in cursor:
    
     m_distance = document['distance']
     m_run_number = document['run_number']
     m_angle = float(document['angle'])
     m_robot= document['robot_id']
     m_distance_list = document['distance_list']
     m_decision = document['decision']
    
     logging.info("decision: " + str(m_decision))
     logging.info("distance: "+ str(m_distance))
     #logging.info("raw angle: " + str(m_angle))
     logging.info("coords: " + str(robot_x) + ", " + str(robot_y))
    
     frac, whole = math.modf(abs(round(m_angle / 360, 2)))
     #logging.info(frac)
     #Which direction are we heading
     if m_angle > 0:
         s_type = 'positive'
     else:
         s_type = 'negative'
     #get degree
     deg = 0
     if frac == 0:
         deg = 0
     if s_type == 'positive' and frac == .25:
         deg = 90
     if s_type == 'negative' and frac == .25:
         deg = 270
     if s_type == 'positive' and frac == .75:
         deg = 270
     if s_type == 'negative' and frac == .75:
         deg = 90
     if frac == .5:
         deg = 180
    
     logging.info("calc angle: " + str(deg))
     #Pull Angles & Distances
     for a_ang, a_dist in m_distance_list.iteritems():
          if( float(a_ang) % 10 == 0):
                #Calculate XYs
                myX = round((float(a_dist)*math.cos(((float(a_ang)+20)*math.pi/180))),2)
                myY = round((float(a_dist)*math.sin(((float(a_ang)+20)*math.pi/180))),2)
        
                graphX.append(myX)
                graphY.append(myY)
        
        
     plt.plot(graphX,graphY,'x')
     plt.show()
     graphX = []
     graphY = []
     #break 

#if deg== 0:
            #0
        #    graphX.append(myX)
        #    graphY.append(myY + y_adjustment)
            #print( " orig: " + str(myX) + ", " + str(myY) + " new: " + str(myX) + ", " + str(myY+y_adjustment))
        #if deg == 270:
            #270     
        #    graphX.append(myY*-1)
        #    graphY.append(myX)  
        
        #if deg == 90: 
            #90    
        #    graphX.append(myY)
        #    graphY.append(myX*-1)
        
        #if deg == 180:
            #180
        #    graphX.append(myX*-1)
        #    grapyY.append(myY*-1)
    
    #print("-----------------------------------")
    #if deg == 0:
    #    robot_y = robot_y - m_distance
    #    y_adjustment = y_adjustment + m_distance
  