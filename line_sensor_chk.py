#!/usr/bin/env python
# Dexter Industries line sensor basic example
#
# This example shows a bsic example to read sensor data from the line sensor
#
# Have a question about this example?  Ask on the forums here:  http://www.dexterindustries.com/forum/?forum=grovepi
#
# Karan Nayan
# Initial Date: 13 Dec 2015
# Last Updated: 13 Dec 2015
# http://www.dexterindustries.com/
'''
## License
 Copyright (C) 2015  Dexter Industries
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''

import line_sensor
import time

def get_sensorval():
	while True:
		val=line_sensor.read_sensor()
		if val[0]<>-1:
			return val
		#else:
			#Read once more to clear buffer and remove junk values
		#	val=line_sensor.read_sensor()
count = 0
while True:
	l0,l1,l2,l3,l4=get_sensorval()
	print l0,l1,l2,l3,l4

