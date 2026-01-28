import cv2
import numpy as np

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:

    _, img = capture.read()

    imgCanny = cv2.Canny(img, 100,100)

    kernel = np.ones((5,5), np.uint8)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

    cv2.imshow("webcam", img)
    cv2.imshow("imgCanny", imgCanny)
    cv2.imshow("imgdilate", imgDilation)
    if cv2.waitKey(20) & 0xff == ord('p'):
        break

capture.release()
cv2.destroyAllWindows()