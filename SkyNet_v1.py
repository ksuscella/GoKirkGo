from gopigo import *
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
    for servo_pos in xrange(start_scan,deg_scan,increm):
        servo(servo_pos)
        time.sleep(.02)
        dist=us_dist(15)			#Find the distance of the object in front
        situation[i] = dist

def decision():
    #Step 1 - Lets see if we can go straight
    middle = deg_scan/2 
    
    #Should we go straight?
    if situation[middle] > stop_distance:
        #move forward
        print("moving forward " + str(situation[middle]) + "cm")
        move_forward()
    elif situation[deg_scan-increm] > stop_distance:
        #move left?
        print("moving left " + str(situation[deg_scan-increm]) + "cm")
        turn_left()
    elif situation[start_scan] > stop_distance:
        #move right?
        print("moving right " + str(situation[start_scan])+"cm")
        turn_right()
    else:
        print("turning around")

def move_forward():
    #GoPiGo moves forward a short distance
	enc_tgt(1,1,18)	#Set encoder targetting. Stop after 4 rotations of both the wheels
	fwd()
	time.sleep(.2)
def move_backward():
    #GoPiGo moves backward a short distance
    enc_tgt(1,1,18) #Set encoder targetting.  Stop after 4 rotations of both the wheels
    bwd()
def turn_left():
    left_rot()
def turn_right():
    right_rot()

print "Press ENTER to begin"
raw_input()				#Wait for input to start

while True:
    servo()
    decision()
    time.sleep(1)
    tracker = tracker + 1
    if tracker > 10:
        break

