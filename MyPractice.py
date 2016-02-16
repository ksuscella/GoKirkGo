#!/usr/bin/env python
#############################################################################################################                                                                  
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)


print sys.argv[0]
print sys.argv[1]
print sys.argv[1:]

arguments = sys.argv[1:]

print float(arguments[0])

for a in arguments:
    print(a)
    

