import cv2

faceCascade = cv2.CascadeClassifier('/Users/kirk/Documents/GoPiGo/GoKirkGo/haarcascade_frontalface_default.xml')


# Load image from disk
#frame = cv2.imread('/Users/kirk/Documents/GoPiGo/GoKirkGo/onWeb.png')
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Load image from webcam
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', rgb)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        gray = cv2.imwrite('capture.jpg', frame)
        break

faces = faceCascade.detectMultiScale(
    rgb,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)
print(faces)
# Draw a rectangle around the faces
faceNo=0
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    faceNo +=1
#Evaluate Faces
print("Number of Faces Detected: "+str(faceNo))

#Save Image
out = cv2.imwrite('/Users/kirk/Documents/GoPiGo/GoKirkGo/onWeb2.png',frame)
print(out)