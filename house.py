import cv2
import numpy as np
image = np.ones((500,800,3),dtype=np.uint8)*255
image = cv2.rectangle(image,(150,150),(450,450),(200,150,200),5)
image = cv2.line(image,(150,150),(300,50),(20,20,200),3)
image = cv2.line(image,(450,150),(300,50),(20,20,200),3)
image = cv2.rectangle(image,(200,200),(250,250),(200,100,100),2)
cv2.imshow("canvas",image)
cv2.waitKey(0)