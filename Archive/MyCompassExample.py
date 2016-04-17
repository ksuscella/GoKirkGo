from grove_compass_lib import *
from gopigo import *

c=compass()

c.update()
print(c.headingDegrees)	# compass counts go from 360 -> 0 when turning left, so invert the count

			