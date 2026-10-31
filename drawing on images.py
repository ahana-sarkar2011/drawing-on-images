import cv2
pika = cv2.imread("lesson 4-drawing on images/images/pika.png")
pika = cv2.line(pika,(191,0),(0,263),(200,50,3),5)
pika = cv2.rectangle(pika,(20,30),(171,233),(150,100,20),3)
pika = cv2.circle(pika,(80,70),20,(100,3,150),0)
pika = cv2.circle(pika,(110,150),15,(100,200,100),-1)
pika = cv2.putText(pika,"pika",(30,22),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(150,10,150),2,cv2.LINE_4)
cv2.imshow("pika with line",pika) 
cv2.waitKey(0)