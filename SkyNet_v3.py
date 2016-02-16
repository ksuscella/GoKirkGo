from gopigo import *
import random
import math
import sys
import time

#argument variables (pass in as args to callibrate)
# -- --------------------------
arg_stop_dist = 40
arg_rot_fwd = 18
arg_rot_side = 9
arg_rot_bck = 18
arg_robot_speed = 150
arg_decisions = 10
# -- ---------------------------

full_scan = 180
deg_scan = 140
start_scan=40
increm = 10
tracker=0   
situation = {}

def servo_int():
    #Run Through Scan
    for servo_pos in xrange(start_scan,deg_scan,increm):
        servo(servo_pos)
        time.sleep(.02)
        dist=us_dist(15)			#Find the distance of the object in front
        situation[servo_pos] = dist
        
def decision():
    #Step 1 - Lets see if we can go straight
    middle = full_scan/2 
    
    #Should we go straight?
    if situation[middle] > arg_stop_dist:
        #move forward
        print("moving forward " + str(situation[middle]) + "cm")
        move_forward()
    elif situation[deg_scan-increm] > arg_stop_dist:
        #move left?
        print("moving left " + str(situation[deg_scan-increm]) + "cm")
        turn_left()
    elif situation[start_scan] > arg_stop_dist:
        #move right?
        print("moving right " + str(situation[start_scan])+"cm")
        turn_right()
    else:
        print("turning around")
        turn_around()

def move_forward():
    #GoPiGo moves forward a short distance
    enc_tgt(1,1,arg_rot_fwd)
    fwd()
    
def turn_around():
    #Turn Around
    
    #Pick which way to turn
    if situation[deg_scan-increm] > situation[start_scan]:
        enc_tgt(1,1,arg_rot_bck)
        left_rot()
    else:
        enc_tgt(1,1,arg_rot_bck)
        right_rot()
    
def turn_left():
    #Turn Left
    enc_tgt(1,1,arg_rot_side)
    left_rot()
    
def turn_right():
    #Turn Right
    enc_tgt(1,1,arg_rot_side)
    right_rot()

### PASS IN ARGUMENTS ###
#0 - STOP DISTANCE
#1 - FORWARD (ROTATIONS)
#2 - SIDE (ROTATIONS)
#3 - BACK (ROTATIONS)
#4 - SET SPEED
#5 - NUMBER OF DECISION ITERATIONS

args = sys.argv[1:] #Get Arguments
if len(args) == 6:  #Use defaults if arguments don't match
    #Take Arguments
    arg_stop_dist = int(args[0])
    arg_rot_fwd = int(args[1])
    arg_rot_side = int(args[2])
    arg_rot_bck = int(args[3])
    arg_robot_speed = int(args[4])
    arg_decisions = int(args[5])


print "Press ENTER to begin"
raw_input()				#Wait for input to start
set_speed(arg_robot_speed)

while True:
    servo_int()
    decision()
    time.sleep(1)
    stop()
    tracker = tracker + 1
    if tracker > arg_decisions:
        break

