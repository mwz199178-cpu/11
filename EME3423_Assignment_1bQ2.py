import cv2

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:

    _, img = capture.read()

    imgCanny = cv2.Canny(img, 100,100)

    imgBlur = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)

    imgHSV = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

    cv2.imshow("webcam", img)
    cv2.imshow("imgCanny", imgCanny)
    cv2.imshow("imgBlur",imgBlur)
    cv2.imshow("imgHSV",imgHSV)
    if cv2.waitKey(20) & 0xff == ord('p'):
        break

capture.release()
cv2.destroyAllWindows()