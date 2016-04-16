import cv2
import urllib                   # Send Info to Laptop
import urllib2                  # Send Info to Laptop
import base64
import requests

my_mac = 'localhost:8889' #localhost

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    cv2.imshow('frame', rgb)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        small = cv2.resize(frame, (0,0), fx=0.1, fy=0.1)
        out = cv2.imwrite('capture.jpg', small)
        break

f = open("/Users/kirk/Documents/GoPiGo/GoKirkGo/capture.jpg")
data = f.read()
f.close()



test = base64.b64encode(data)    

#Send findings to laptop
url = 'http://' + my_mac + '/'
url = url + '?get_image='+test
response = requests.get(url)

cap.release()
cv2.destroyAllWindows()