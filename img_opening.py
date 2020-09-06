import cv2 as c 
import numpy as np
import matplotlib.pyplot as pt

imgpath = 'download.jpeg'
img = c.imread(imgpath,1)

pt.imshow(img)
pt.title('iPhones')
pt.show()


print(img)
