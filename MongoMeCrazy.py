#MongoDB Me Crazy - Practice Python File

from pymongo import MongoClient
import pymongo
import json
import math
import matplotlib.pyplot as plt
import numpy as np

client = MongoClient()
db = client.kirk

#Last run 20160304035759
cursor = db.robot.find(
        {"run_number": 20160304035759}
        ).sort([
        ("decision", pymongo.ASCENDING)])

graphX = []
graphY = []

x_adjustment=0
y_adjustment=0
    
for document in cursor:
    #Set some temporary variables to pull data
    m_distance = document['distance']
    m_run_number = document['run_number']
    m_angle = document['angle']
    m_robot= document['robot_id']
    m_distance_list = document['distance_list']
    m_decision = document['decision']
    
    #Pull Angles & Distances
    for a_ang, a_dist in m_distance_list.iteritems():
        
        #Calculate XYs
        myX = (float(a_dist)*math.cos(math.pi*(float(a_ang))/180))
        myY = (float(a_dist)*math.sin(math.pi*(float(a_ang))/180))
        
        if (m_angle=='start'):
                graphX.append(myX)
                graphY.append(myY)
        if (m_angle=='forward'):
                y_adjustment = y_adjustment - m_distance
                graphX.append(myX)
                graphY.append(myY+y_adjustment)
        if (m_angle=='left'):
                graphX.append(myY*-1)
                graphY.append(myX)
        if (m_angle=='right'):
                graphX.append(myY)
                graphY.append(myX*-1)
        
    print(" " + str(m_angle))          
    print(" " + str(m_distance))
    
    
plt.plot(graphX,graphY,'x')
plt.show()