import cv2 

def main() : 
    cv2.namedWindow('Live Video Feed')
    cap = cv2.VideoCapture(0) 

    if cap.isOpened() : 
        ret, frame = cap.read()

    else : 
        ret = False 

    while True : 
        ret, frame = cap.read() 
        cv2.imshow('Live Video Feed',frame)
        if (cv2.waitKey(1) == 27) : 
            break

    cv2.destroyWindow('Live Video Feed')
    cap.release() 

main()