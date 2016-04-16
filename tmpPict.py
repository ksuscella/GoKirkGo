import base64
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    cv2.imshow('frame', rgb)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        small = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        out = cv2.imwrite('capture.jpg', small)
        break

    f = open("/Users/kirk/Documents/GoPiGo/GoKirkGo/capture.jpg")
    data = f.read()
    f.close()

    string = base64.b64encode(data)
    string = str(string).encode('utf-8')
    convert = base64.b64decode(string)

    t = open("/Users/kirk/Documents/GoPiGo/GoKirkGo/capture2.jpg", "w+")
    t.write(convert)
    t.close()
