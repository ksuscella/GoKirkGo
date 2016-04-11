import cv2
import urllib                   # Send Info to Laptop
import urllib2                  # Send Info to Laptop
import base64

my_mac = 'localhost:8889' #localhost

j_robot_number=1
j_run_number=1
j_angle=90
j_distance=100
j_decision="test"

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    cv2.imshow('frame', rgb)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite('capture.jpg', frame)
        break

#print(frame)
small = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
test = base64.b64encode(small)
# Collect up all distances & angles
# numpy.ndarray    
#Setup Full Json    
json_string = ('{' + 
'"robot_id":' + str(j_robot_number) + ',' +
'"run_number":' + str(j_run_number) + ',' +
'"angle":' + '\"' + str(j_angle) + '\"' + ',' +
'"distance":' + str(j_distance) + ',' +
'"image":' + test + '}')

#Send findings to laptop
url = 'http://' + my_mac + '/'
url = url + '?get_json='+json_string

#print(url)
req = urllib2.Request(url)
f = urllib2.urlopen(req)
response = f.read()
print(response)
f.close()

cap.release()
cv2.destroyAllWindows()