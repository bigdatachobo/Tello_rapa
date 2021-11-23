from djitellopy import Tello, tello
import cv2 as cv

tello = Tello()
tello.connect()

# 패널
stream = cv.imread('./tello_img.jpg')
cv.imshow('Tello image',stream)

# 기본 이동거리 및 회전각
length = 50
angle = 90

# keyboard control
while True:
    key = cv.waitKey(0)
    if key == ord('t'): # takeoff - 이륙
        tello.takeoff()
    elif key == ord('e'): # land - 착륙
        tello.land()
    
    # 좌측 조이스틱
    elif key == ord('w'): # up - 고도 상승
        tello.move_up(length)
    elif key == ord('s'): # down - 고도 하강
        tello.move_down(length)
    elif key == ord('d'): # cw - 시계 회전
        tello.rotate_clockwise(angle)
    elif key == ord('a'): # ccw -  반시계 회전  
        tello.rotate_counter_clockwise(angle)
    
    # 우측 조이스틱             
    elif key == ord('i'): # forward - 전진
        tello.move_forward(length)
    elif key == ord('k'): # back - 후진
        tello.move_back(length)
    elif key == ord('j'): # left - 좌측 이동
        tello.move_left(length)
    elif key == ord('l'): # right - 우측 이동
        tello.move_right(length)
        
    # 상태 체크
    elif key == ord('b'): # battery 체크
        tello.get_battery()
    
    # 종료     
    elif key == ord('q'):
        break