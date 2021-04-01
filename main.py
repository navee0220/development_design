
import numpy as np
import cv2
''' 
image = cv2.imread('line.PNG',1)
mark = np.copy(image) '''

def region_of_interest(img,vertices,color3=(255,255,255),color1=255):

    mask = np.zeros_like(img)

    if len(img.shape) > 2:
        color = color3
    else:
        color = color1


    cv2.fillPoly(mask,vertices,color)

    ROI_image = cv2.bitwise_and(img,mask)

    return ROI_image

def mark_img(img,blue_threshold = 200,green_threshold = 200,red_threshold = 200):

    bgr_threshold = [blue_threshold,green_threshold,red_threshold]

    
    thresholds = (image[:,:,0] < bgr_threshold[0]) \
                | (image[:,:,1] < bgr_threshold[1]) \
                | (image[:,:,2] < bgr_threshold[2])

    mark[thresholds] = [0,0,0]

    return mark


cap = cv2.VideoCapture('road.mp4')

while(cap.isOpened()):

    ret, image = cap.read()


    vertices = np.array([[(820,630),(460,980),(1610,980),(1120,630)]],dtype=int)

    roi_img = region_of_interest(image,vertices,(0,0,255))

    mark = np.copy(roi_img)
    mark = mark_img(roi_img)

    color_threshold = (mark[:,:,0]==0) & (mark[:,:,1]==0) & (mark[:,:,2] > 200)

    
    image[color_threshold] = [0,0,255]

    cv2.imshow('results',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
