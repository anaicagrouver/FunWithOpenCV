from tkinter import *
import cv2
import numpy as np

root = Tk() 
uframe = Frame(root,width=3000, height=2000, bg = 'blue')
uframe.pack()
label = Label(uframe, 
		 text="Mini Project \n",
		 fg = "light green",
		 font = "Helvetica 16 bold italic",bg = 'blue')
label.pack()
root.title("Mini project")

def func() : 
    pass
def blending () : 
    img1 = cv2.imread('download.jpeg',1)
    print(img1)
    img2 = cv2.imread('apple.jpg',1)
    alpha, beta = 1,0
    #img1 = cv2.resize(img1, (100,100))
    #img2 = cv2.resize(img2, (100,100))
    blend_img = cv2.addWeighted(img1, alpha, img2, beta,0)
    cv2.namedWindow('transition')
    cv2.createTrackbar('bar','transition', 0,10,func) 
    while(True) :
        
        cv2.imshow('transition', blend_img)
        
        if cv2.waitKey(1) == 27:
            break
        
        alpha = cv2.getTrackbarPos('bar', 'transition') / 10
        beta = 1 - alpha
        
        blend_img = cv2.addWeighted(img1, alpha, img2, beta, 0)
        
    cv2.destroyAllWindows() 

def negative () : 

    imgpath = 'download.jpeg'
    img = cv2.imread(imgpath,1)
    img1 = abs(255-img)
    print(img)
    cv2.imshow('Actual Image', img)
    cv2.imshow('Negative Image',img1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def tracking() : 
    cv2.namedWindow('Live Video Feed')
    cap = cv2.VideoCapture(0) 
    ret = True
    while ret : 
        ret, frame = cap.read() 
        low = np.array([100,50,50]) 
        high = np.array([150,255,255])
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


button1 = Button(uframe, text="Image Blending",fg = "purple",command = blending) 
button1.pack(side = RIGHT)

button2 = Button(uframe, text="Negative of the image",fg = "purple",command = negative) 
button2.pack(side = LEFT)

button3= Button(uframe, text="Tracking Blue Objects",fg = "purple",command = tracking) 
button3.pack(side = LEFT)

root.mainloop() 
