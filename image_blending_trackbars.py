import cv2
import matplotlib as pt 
def func() : 
    pass
def main () : 
    img1 = cv2.imread('download.jpeg',1)
    img2 = cv2.imread('apple.jpg',1)
    alpha, beta = 1,0
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
        
        print (alpha, beta)
        
    cv2.destroyAllWindows()


    
main()
