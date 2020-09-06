import cv2
import matplotlib.pyplot as pt 
import numpy as np 
import time
def main () : 
    img1 = cv2.imread('download.jpeg',1)
    img2 = cv2.imread('apple.jpg',1)

    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) 
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) 
    alpha, beta = 1,0
    img1 = cv2.resize(img1, (100, 50)) 
    img2 = cv2.resize(img2,(100,50)
    for i in np.linspace(0,1,10) : 
        output = cv2.addWeighted(img1, alpha, img2, beta,0)
        alpha = i 
        beta = 1-i
        cv2.imshow('transition', output)
        time.sleep(2)
        print('hell')
        if cv2.waitKey(1) == 27 : 
            break 
    cv2.destroyWindow("transition")
    
    
    '''titles = ['imgage one','image two','blended image']
    img = [img1, img2, output]

    for i in range(len(img)) : 
        pt.subplot(1,len(img),i+1) 
        pt.title(titles[i])
        pt.imshow(img[i])
        pt.xticks([])
        pt.yticks([])

    pt.show()
    print('hello')'''

main()