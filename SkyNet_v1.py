from gopigo import *
import random
import math
import sys
import time

full_scan = 180
deg_scan = 140
start_scan=40
increm = 10
stop_distance = 20
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
    enc_tgt(1,1,18)
    fwd()
    time.sleep(1)
    stop()
    
def move_backward():
    #GoPiGo moves backward a short distance
    left()
    time.sleep(.5)
    left()
    time.sleep(.5)
    stop()
    
def turn_left():
    left()
    time.sleep(.5)
    stop()
def turn_right():
    right()
    time.sleep(.5)
    stop()

print "Press ENTER to begin"
raw_input()				#Wait for input to start
set_speed(150)

while True:
    servo_int()
    decision()
    time.sleep(1)
    tracker = tracker + 1
    if tracker > 10:
        break

