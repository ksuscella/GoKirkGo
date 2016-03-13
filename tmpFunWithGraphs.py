#Fun with Graphs

import json
import math
import matplotlib.pyplot as plt
import numpy as np

graphX = []
graphY = []

myCoords = set()
myCoords.add((5,30))
myCoords.add((-5,30))
myCoords.add((10,35))
myCoords.add((-10,35))
myCoords.add((15,20))
myCoords.add((-15,20))

for myCoord in myCoords:
    #Straight On
    graphX.append(myCoord[0])
    graphY.append(myCoord[1])

    # -90 degrees
    # Negative & Flip
    graphX.append(myCoord[1]*-1)
    graphY.append(myCoord[0])

    # +90 degrees
    # Positive & Flip
    graphX.append(myCoord[1])
    graphY.append(myCoord[0]*-1)

    # 180 degrees
    graphX.append(myCoord[0]*-1)
    graphY.append(myCoord[1]*-1)

#bogus coordinates to strech graph
graphX.append(50)
graphY.append(50)
graphX.append(-50)
graphY.append(-50)

ax = plt.gca()
ax.grid(True)

plt.plot(graphX,graphY,'x')
plt.show()