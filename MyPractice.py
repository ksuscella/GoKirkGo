#!/usr/bin/env python
#############################################################################################################                                                                  
import random

situation = {}
side1 = []
side2 = []
stop_dist = 30

stuck = 0

for servo_pos in xrange(10,170,10):
    situation[servo_pos] = random.randint(20,50)

if stuck > 3:
    print("break - we are stuck")

# Going Forward Direction?
if situation[90] > stop_dist:
    
    # Lets sniff +/- 30' of 90 to see if anything is in our way
    for ang in range(80, 50, -10):
        side1.append(situation[ang])
    
    if min(side1) < stop_dist:
        good1 = False
    else:
        good1 = True
    
    for ang in range(100, 130, 10):
        side2.append(situation[ang])
    
    if min(side2) < stop_dist:
        good2 = False
    else:
        good2 = True
    
    if good1 == True and good2 == True:        
        goDist = situation[90] - stop_dist
        print ("Go Straight " + str(goDist) + "cm")
        stuck = 0 #We went forward, reset counter

# Have we rotated more than 3 time without going forward (stuck?)

# Go Left or Right?
stuck += 1


# Turn Around?
stuck += 1


#To Do - I want to check and make some adjustments if angles are wackie