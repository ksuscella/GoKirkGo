import random
import math
import sys
import time

deg_scan = 180
start_scan=10
increm = 10
stop_distance = 20
tracker=0   
situation = {}

def servo():
    #Run Through Scan
    for i in xrange(start_scan,deg_scan,increm):         #loop by 20
        situation[i] = random.randint(0,30)
    print(situation)

def decision():
    #Step 1 - Lets see if we can go straight
    middle = deg_scan/2 
    
    #Should we go straight?
    if situation[middle] > stop_distance:
        #move forward
        print("moving forward " + str(situation[middle]) + "cm")
        
    elif situation[deg_scan-increm] > stop_distance:
        #move left?
        print("moving left " + str(situation[deg_scan-increm]) + "cm")
        
    elif situation[start_scan] > stop_distance:
        #move right?
        print("moving right " + str(situation[start_scan])+"cm")
    
    else:
        print("turning around")


while True:
    servo()
    decision()
    time.sleep(1)
    tracker = tracker + 1
    if tracker > 10:
        break



        