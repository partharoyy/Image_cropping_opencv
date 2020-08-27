import cv2
import numpy as np

img = np.zeros((512,512,3), dtype=np.uint8) # creating a black background to capture the mouse events

windowName = "Drawing"
cv2.namedWindow(windowName)  #we have to pass the image name into namedWindow

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 30, (0, 0, 255), -1) #we are telling here to draw a circle on the black image we created above, x and y are pointing the centre of the circle,
    if event == cv2.EVENT_RBUTTONDOWN:  #30 is the radius and -1 is to fill the circle inside
        cv2.circle(img, (x,y), 20, (0, 255, 0), -1)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 50, (255, 0, 0), -1)                                                

cv2.setMouseCallback(windowName, draw_circle) #takes 2 variables


while True:

    cv2.imshow(windowName, img)
    if cv2.waitKey(10) == ord("q"):
        break

cv2.destroyAllWindows()