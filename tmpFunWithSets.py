
myPaths = [] #x,y,angle


myPaths.append((2,3))
myPaths.append((3,5))

print(myPaths)

sorted(myPaths, key=getKey)

#for mypath in myPaths:  
#    print(str(mypath[0]) + " " +str(mypath[1]))



def getKey(item):
        return item[0]