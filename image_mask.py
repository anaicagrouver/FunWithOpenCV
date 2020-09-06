import cv2 
import numpy as np

def main() : 
    cv2.namedWindow('Live Video Feed')
    cap = cv2.VideoCapture(0) 
    ret = True
    while ret : 
        ret, frame = cap.read() 
        #peach-red
        #low = np.array([0,100,100])
        #high = np.array([20,255,255])
        #white
        #green
        low = np.array([40, 40, 40])
        high = np.array([70,255,255])
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        image_mask = cv2.inRange(hsv,low,high)
        output = cv2.bitwise_and(frame,frame, mask = image_mask)
        cv2.imshow('Union', output)
        cv2.imshow('Image Mask',image_mask)
        cv2.imshow('Live Video Feed',frame)
        if (cv2.waitKey(1) == 27) : 
            break

    cv2.destroyAllWindows()
    cap.release() 

main()
