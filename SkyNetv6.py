from gopigo import *
# ###########################################################################################
# Project for an autonomous robot
# ###########################################################################################

import random
import math
import sys
import time

import urllib                   # Send Info to Laptop
import urllib2                  # Send Info to Laptop
import time                     # Create unique run id

#argument variables (pass in as args to callibrate)
# -- --------------------------
arg_stop_dist = 30              # cm robot stops
arg_rot_fwd = 20                # number of encoder going fwd (roughly 1 per cm)
arg_rot_side = 8                # number of encoder to make a 90 turn
arg_rot_bck = 16                # number of encoder to make a 180 turn
arg_robot_speed = 150           # Speed
arg_decisions = 5              # Number of times we loop through the program before breaking
# -- ---------------------------

#Fixed variables
# -- ---------------------------
full_scan = 180                 # Full Degree range with servo
end_servo_pos = 180                  # Degree to finish from (due to mounting)
middle_scan = 90                # Degree looking forward (90 is not straight - using 70)
start_servo_pos=0                    # Degree to start from (due to mounting)
increm = 20                     # Degrees to increment via servo
sample =7                      # Capture more than one distance
tracker=0                       # Keeps track of number of times we have looped
situation = {}                  # keep track of all the distances
turn_track = 0                  # how many times have we turned & not gone forward
# -- ---------------------------

# URL variables
# -- ---------------------------
j_robot_number = 1								#Static robot #
j_run_number = time.strftime("%Y%m%d%H%M%S")    #Static to the Application Run
j_angle = 0     								#Static for now - angle relative to start
j_distance = 0									#Static for now - distance travelled
j_xcoord = 0                                    #Robots Location
j_ycoord = 0                                    #Robots Location
j_decision = 0									#Static for now - number of times the robot has made a decision on scan
my_mac = '192.168.1.102:8889'
# -- ---------------------------

def servo_int():
    #Run through scan angles and capture results
    for a_ang in xrange(start_servo_pos,end_servo_pos+increm,increm):
        dist_l = []
        servo(a_ang)
        avg_sum = 0
        #disable_servo()     # Noticed shaking....try to stabilize
        time.sleep(.25)      # Give it time to get into position
        
        for a_sample in xrange(1,sample+1,1):
            avg_sum = avg_sum + us_dist(15)
            dist_l.append(us_dist(15))
        #Remove min/max numbers - its fine if the number dup
        dist_l.remove(max(dist_l))
        dist_l.remove(min(dist_l))
        dist = sum(dist_l) / float(len(dist_l))
        situation[a_ang] = dist

def send_info():
    #Send results to laptop
    j_decision = tracker
    # Collect up all distances & angles
    json_scans = '{'
    for a_ang in xrange(start_servo_pos,end_servo_pos+increm,increm):
        json_scans = json_scans + "\""+str(a_ang)+"\":" + str(situation[a_ang]) + ","
    
    trim_length = len(json_scans)-1	#trim comma out
    json_scans = json_scans[:trim_length] + "}"
        
    #Setup Full Json    
    json_string = ('{' + 
	'"robot_id":' + str(j_robot_number) + ',' +
	'"run_number":' + str(j_run_number) + ',' +
	'"angle":' + '\"' + str(j_angle) + '\"' + ',' +
	'"distance":' + str(j_distance) + ',' +
	'"decision":' + str(j_decision) + ',' +
	'"distance_list":' + json_scans + '}')
    
    #Send findings to laptop
    url = 'http://' + my_mac + '/'
    url = url + '?get_json='+json_string
    
    print(url)
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    response = f.read()
    print(response)
    f.close()

def full_straight():
    # Scan forward direction
    fwd_scan = []
    
    # Take middle angle +/- 30 degrees
    for ang in range(middle_scan-30, middle_scan+40, 10):
        fwd_scan.append(situation[ang])
    
    if (min(fwd_scan) > arg_stop_dist):
        return True
    else:
        return False

def full_turn(side):
    side1 = []
    # Test to see if a side angle is the right way to go 
    if (side=="left"):
        for ang in range(end_servo_pos, end_servo_pos-30, -10):
            side1.append(situation[ang])
    elif (side=="right"):
        for ang in range(start_servo_pos,start_servo_pos+30, 10):
            side1.append(situation[ang])
     
    print(side + " " + str(min(side1))) 
    if ( min(side1) > arg_stop_dist):
        return True
    else:
        return False
     
def decision():
    global j_angle 
    # Step 1 - Should we go straight?
    if full_straight(): #move forward?
        print("moving forward " + str(situation[middle_scan]) + "cm")
        #j_angle = "forward" -- doesn't change
        move_forward()
    # Step 2 - Try Left?
    elif full_turn("left"): #move left?
        print("moving left " + str(situation[end_servo_pos-increm]) + "cm")
        j_angle = j_angle - 90
        turn_left()
    # Step 3 - Try Right?
    elif full_turn("right"): #move right?
        print("moving right " + str(situation[start_servo_pos])+"cm")
        j_angle = j_angle + 90
        turn_right()
    # Step 4 - Turn Around
    else:
        print("turning around")
        j_angle = j_angle+180
        turn_around()

    
def move_forward():
    global j_distance 
    #GoPiGo moves forward a short distance
    fwd_rot = situation[middle_scan] - arg_stop_dist 
    if (fwd_rot < arg_rot_fwd):
        j_distance = fwd_rot
        enc_tgt(1,1,fwd_rot)
    else:
        j_distance = arg_rot_fwd
        enc_tgt(1,1,arg_rot_fwd)
    print(j_distance)
    fwd()
    
def turn_around():
    #Turn Around
    global j_distance
    j_distance = 0
    enc_tgt(1,1,arg_rot_bck)
    left_rot()
    
def turn_left():
    #Turn Left
    global j_distance
    j_distance = 0
    enc_tgt(1,1,arg_rot_side)
    left_rot()
    
def turn_right():
    #Turn Right
    global j_distance
    j_distance = 0
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
enable_servo()

while True:
    servo_int()
    #decision()
    send_info()
    time.sleep(1) 
    tracker = tracker + 1
    if tracker > arg_decisions:
        break
    
disable_servo()

