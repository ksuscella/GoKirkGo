import cv2
import numpy as np
from matplotlib import pyplot as plt

# Windows dependencies
# - Python 2.7.6: http://www.python.org/download/
# - OpenCV: http://opencv.org/
# - Numpy -- get numpy from here because the official builds don't support x64:
#   http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

# Mac Dependencies
# - brew install python
# - pip install numpy
# - brew tap homebrew/science
# - brew install opencv

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    cv2.imshow('frame', rgb)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite('capture.jpg', frame)
        print("captured image")
        break

cv2.imwrite('testphoto.png', out)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', out)
#small = cv2.resize(out, (0,0), fx=0.5, fy=0.5)
#plt.imshow(small, cmap='gray', interpolation='bicubic')
#plt.xticks([]), plit.yticks([]) # to hide tick values on x and y axis
#plt.show()

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()