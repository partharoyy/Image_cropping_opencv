import cv2
import numpy as np # import important libraries

img = cv2.imread('mickey.jpg') # Using imread function to copy the original image and storing in img variable


height, width = img.shape[:2]  #storing values of height and width of the image in below variables


cv2.imshow('Original',img) #displaying the image
cv2.waitKey(0) # this will display the image until any key is pressed

cv2.destroyAllWindows() # when a key is pressed this will destroy all active windows

#Hardcoded image crop

#starting point
x1,y1 = int(height * 0.25), int(width * 0.25)     #note here is x1 stores height whereas it seems it should store width because x resembles horizontal axis
                                                  # but we have to remember in case of image height always comes first so x1,x2 will store height coordinates
#End point
x2,y2 = int(height * 0.75), int(width * 0.75)

crop = img[x1:x2,y1:y2]

cv2.imshow('Cropped',crop)
cv2.waitKey(0)
cv2.destroyAllWindows()