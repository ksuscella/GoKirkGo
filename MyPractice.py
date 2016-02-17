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
    side1.append(situation[90-10])
    side1.append(situation[90-20])
    side1.append(situation[90-30])
    good1 = True
    for a_angle in side1:
        if a_angle < stop_dist:
            good1 = False
    
    side2.append(situation[90+10])
    side2.append(situation[90+20])
    side2.append(situation[90+30])
    good2 = True
    for a_angle in side2:
        if a_angle < stop_dist:
            good2 = False
    
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