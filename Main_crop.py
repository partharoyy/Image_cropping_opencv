import cv2
import numpy as np


ref_point = []    #empty list to store x and y coordinates

def shape_selection(event, x, y, flags, param):
    global ref_point, crop    #to call above variables inside a function we need to write global keyword

    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x,y)]    #fetching coordinates(x,y) when left mouse button is pressed
    
    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x,y)) 
        print(ref_point)
        cv2.rectangle(image, ref_point[0], ref_point[1], (150,50,115), 3)    #3 is the border width
        cv2.imshow('image', image)


image = cv2.imread('mickey.jpg')
clone = image.copy()
cv2.namedWindow('image')
cv2.setMouseCallback('image', shape_selection)

while True:
    cv2.imshow('image', image)
    k = cv2.waitKey(10)

    if k == ord('r'):
        image = clone.copy()

    if k == ord('q'):
        break

if len(ref_point) == 2:
    crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
    cv2.imshow('Cropped Image', crop_img)
    cv2.imwrite('Cropped_image.png', crop_img) #to save the cropped image in the current directory
    cv2.waitKey(0)

cv2.destroyAllWindows()