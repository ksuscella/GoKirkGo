#Temp

#Write to a file

import os
import json
import time

print(time.strftime("%Y%m%d%H%M%S"))
run_number = time.strftime("%Y%m%d%H%M%S")      #Static to the Application Run
os.chdir("/Users/kirk/Documents/GoPiGo/GoKirkGo/")
f = open('workfile.json', 'a')
f.write("{")
f.write('"robot_id":1,')                        #future when there is more than 1 robot
f.write('"run_number":' + run_number + ',')     #run number for scanning a space
f.write('"angle": 0,')                          #angle relative to the start position
f.write('"distance": 0,')                       #distance travelled before current scan
f.write('"decision_number": 1')
f.write('}')
f.close()


