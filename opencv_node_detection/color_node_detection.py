# -*- coding: utf-8 -*- 


import cv2
import numpy as np
import math
import time



#USB 카메라 연결(초기값 : 0) 및 물건 위치 검사시간설정(6초)
cap = cv2.VideoCapture(0)
max_time = time.time() + 6

while True:

    #카메라를 통해 읽은 영상을 이용해 가우시안 블러(GaussianBlur, 이미지를 흐리게 해 노이즈를 줄인 결과)를 구하고 이를 이용해 hsv 형식의 영상을 만든다.
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)


    '''set the object to catch'''

    #우선 감지할 색상을 진한 파란색으로 설정하였다.
    #lower_blue, upper_blue는 각각 파란색의 범위이다.
    lower_blue = np.array([38, 86, 0])
    upper_blue = np.array([121, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)


    '''define exact object to find'''
    '''cv2.RETR_EXTERNAL finds only outermost contour'''

    _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
 
    '''

    ret, thresh = cv2.threshold(grayFrame, 200, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    '''


    for contour in contours:
        area = cv2.contourArea(contour)
        mmt = cv2.moments(contour)


        if area > 1000:

            cv2.drawContours(frame, contour, -1, (0, 255, 255), 3)


            cx = int(mmt['m10']/mmt['m00'])
            cy = int(mmt['m01']/mmt['m00'])

            x_center = 320
            y_center = 240

            x_error = x_center - cx
            y_error = y_center - cy

            x_object_print = str(x_error)
            y_object_print = str(y_error)



            '''1 : the window to show'''
            cv2.circle(frame, (cx, cy), 10, (0,255,0), -1)
            '''
            cv2.putText(grayFrame, "X: Red/ Y: Blue", (350, 473), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
            '''
            cv2.putText(frame, "x_error : " + x_object_print, (cx, cy-24), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
            cv2.putText(frame, "y_error : " + y_object_print, (cx, cy-12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
            

    '''show the coordinates of contours'''
    '''print(contours)'''
     

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == 27:
        print(x_error, y_error)
        break


cap.release()
cv2.destroyAllWindows()