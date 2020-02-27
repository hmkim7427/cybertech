# -*- coding: utf-8 -*- 


import cv2
import numpy as np
import math
import time
import sys


#USB 카메라 연결(초기값 : 0) 및 물건 위치 검사시간설정(6초)
cap = cv2.VideoCapture(0)
max_time = time.time() + 6

while True:

          
    #카메라로부터 읽은 영상을 이진화 처리한 후(영상을 흑/백을 가지도록) 바꾼 후 두번째 변수(기준이 되는 값, 200)를 기준으로 이보다 크면 세번째 변수의 값(255)으로, 작으면 0으로 처리한다.
    #이후 윤곽선을 그린다. 
    ret, frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grayFrame, 200, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv2.contourArea(contour)
        mmt = cv2.moments(contour)


        #임의로 정한 1000이라는 크기보다 큰 면적만을 다룸으로써 먼지를 비롯한 미세한 오차를 줄였다.
        if area > 1000:

            #앞서 구한 모멘트값(mmt)을 이용하여 중심값 좌표 cx, cy를 구한다. 
            #x_center, y_center는 영상을 띄우는 창의 전체 면적(픽셀, x:0~639, y:0~479)을 기준으로 '임의로' 중심값(창의 중심값이자 물건이 놓여야 할 위치라고 임의로 정함)을 정한 것이다.
            cv2.drawContours(frame, contour, -1, (0, 255, 255), 10)
            cx = int(mmt['m10']/mmt['m00'])
            cy = int(mmt['m01']/mmt['m00'])

            x_center = 320
            y_center = 240

            x_error = x_center - cx
            y_error = y_center - cy

            x_object_print = str(x_error)
            y_object_print = str(y_error)


            #cv2.circle를 이용해 물체의 중심(cx, cy)에 해당하는 위치에 원을 그려 그 위치를 표시하고, cv2.putText를 이용해 중심으로부터 얼마나 떨어져있는지(x_error, y_error) 표시한다.
            cv2.circle(grayFrame, (cx, cy), 10, (0,255,0), 3)
            cv2.putText(grayFrame, "x_error : " + x_object_print, (cx, cy-24), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
            cv2.putText(grayFrame, "y_error : " + y_object_print, (cx, cy-12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))



    #이진화된 영상을 출력한다.
    cv2.imshow('Frame', grayFrame)
    key = cv2.waitKey(1)
    if time.time() > max_time:
        last_error_x = x_error
        last_error_y = y_error



        #물건이 어떤 위치에 놓였는지에 따라 텍스트파일을 만들어 저장한다. 우선 임의로 최대 오차를 3으로 정했으며 이보다 크면 물건이 정해진 위치를 벗어나 잡을 수 없다고 설정하였다.

        if abs(last_error_x) <= 3 and abs(last_error_y) <= 3 :
            sys.stdout = open('output.txt', 'w')
            print("Last error of x : " + str(last_error_x))
            print("Last_error of y : " + str(last_error_y))
            print("x coordinate of object : " + str(cx))
            print("y coordinate of object : " + str(cy))

        else:
            sys.stdout = open('output.txt', 'w')
            print("This object is out of range!!!")




        break

cap.release()
cv2.destroyAllWindows()