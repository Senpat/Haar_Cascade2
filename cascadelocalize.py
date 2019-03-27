#uses the cascade
#cascadetriangle.py video

import sys
import cv2
import numpy as np
import imutils

def localize(x,y,w,h,actualh):
	#in meters
	#vdistance = 16.8438/w 						#vertical distance in meters

	vdistance = 203.712/w
	#print(vdistance)







videopath = "C:/Users/zz198/Desktop/RC/testvideos/whitesquaregopro1.mp4"				#small laptop
#videopath = "C:/Users/zz198/Desktop/RC/testvideos/dronetest1.mp4"

#videopath = "C:/Users/zz198/Desktop/PatrickP/RC/CV/whiteTriangle_Trim.mp4"				#laptank
cap = cv2.VideoCapture(videopath)

triangle_cascade = cv2.CascadeClassifier("triangledata/cascade10.xml")

detected = 0

while True:
	ret,frame = cap.read()
	#frame = imutils.resize(frame,width=704,height=396)
	#frame = imutils.resize(frame,width = 146,height = 86)						#raw is 364,216
	#frame = imutils.resize(frame,width = 80,height = 50)						#for pentagon
	#frame = imutils.resize(frame,width = 364,height=85)
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5,5), 0)
	#ret, gray = cv2.threshold(gray, 250,255,cv2.THRESH_BINARY)
	triangles = triangle_cascade.detectMultiScale(gray,1.25,5)					#(gray,50,1) works best with whiteTriangle_Trim and redtriangle
																				#(gray,1.3,5) works well for differing sizes

	for(x,y,w,h) in triangles:
		#print((x,y,w,h),detected)

		#do canny edge detection on that range
		crop = frame[y:y+h,x:x+w]
		cv2.imshow("crop",crop)
		bin, cnts, _hierarchy = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
		for c in cnts:
			if(cv2.contourArea(c) < 3000):
				continue
			(cx,cy,cw,ch) = cv2.boundingRect(c)
			cv2.rectangle(frame, (cx,cy), (cx+cw, cy+ch), (0,0,255), 2)


		localize(x,y,w,h,-1)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

		detected+=1

	cv2.imshow("frame",frame)

	k = cv2.waitKey(30) & 0xff
	if(k==27):
		break

cap.release()
cv2.destroyAllWindows()

#For triangledata/cascade10.xml
#Arguments		white_triangle detected		redsquare detected
#Goal			163							0
#(gray,50,1)	163
#(gray,50,2)								133
#(gray,50,3)	45							98
#(gray,50,1)	163
#(gray,20,1)	163							171
