import cv2 
import matplotlib.pyplot as pt
def main() : 
    cap = cv2.VideoCapture(0) 

    if cap.isOpened() : 
        ret, frame = cap.read()

    else : 
        print(False)
    
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    pt.imshow(img1)
    pt.title('Color Image RGB')
    pt.show()

    cap.release() 

main()