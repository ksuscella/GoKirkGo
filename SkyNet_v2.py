from gopigo import *
import random
import math
import sys
import time

#argument variables (pass in as args to callibrate)
# -- --------------------------
arg_stop_dist = 20
arg_rot_number = 18
arg_fwd_sleep = 1
arg_LtRt_sleep = .8
arg_turn_sleep = 1.6
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
    enc_tgt(1,1,arg_rot_number)
    fwd()
    time.sleep(arg_fwd_sleep)
    stop()
    
def turn_around():
    #Turn Around
    
    #Pick which way to turn
    if situation[deg_scan-increm] > situation[start_scan]:
        left()
    else:
        right()
    time.sleep(arg_turn_sleep)
    stop()
    
def turn_left():
    #Turn Left
    left()
    time.sleep(arg_LtRt_sleep)
    stop()
    
def turn_right():
    #Turn Right
    right()
    time.sleep(arg_LtRt_sleep)
    stop()

### PASS IN ARGUMENTS ###
#1 - STOP DISTANCE
#2 - FORWARD (ROTATIONS)
#3 - FORWARD (SLEEP)
#4 - LEFT OR RIGHT (SECONDS)
#5 - TURN AROUND (SECONDS)
#6 - SET SPEED
#7 - NUMBER OF DECISION ITERATIONS

args = sys.argv[1:] #Get Arguments
if len(args) == 7:  #Use defaults if arguments don't match
    #Take Arguments
    arg_stop_dist = int(args[0])
    arg_rot_number = int(args[1])
    arg_fwd_sleep = float(args[2])
    arg_LtRt_sleep = float(args[3])
    arg_turn_sleep = float(args[4])
    arg_robot_speed = float(args[5])
    arg_decisions = int(args[6])


print "Press ENTER to begin"
raw_input()				#Wait for input to start
set_speed(arg_robot_speed)

while True:
    servo_int()
    decision()
    time.sleep(1)
    tracker = tracker + 1
    if tracker > arg_decisions:
        break

