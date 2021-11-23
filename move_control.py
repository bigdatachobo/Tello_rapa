from djitellopy import Tello, tello
import cv2 as cv

tello = Tello()
tello.connect()

stream = cv.imread('./tello_img.jpg')
cv.imshow('Tello image',stream)

# keyboard control
while True:
    key = cv.waitKey(0)
    if key == ord('t'): # takeoff - 이륙
        tello.takeoff()
    if key == ord('e'): # land - 착륙
        tello.land()
    
    # 좌측 조이스틱
    if key == ord('w'): # up - 고도 상승
        tello.move_up(20)
    if key == ord('s'): # down - 고도 하강
        tello.move_down(20)
    if key == ord('d'): # cw - 시계 회전
        tello.rotate_clockwise(90)
    if key == ord('a'): # ccw -  반시계 회전  
        tello.rotate_counter_clockwise(90)
    
    # 우측 조이스틱             
    if key == ord('i'): # forward - 전진
        tello.move_forward(20)
    if key == ord('k'): # back - 후진
        tello.move_back(20)
    if key == ord('j'): # left - 좌측 이동
        tello.move_left(20)
    if key == ord('l'): # right - 우측 이동
        tello.move_right(20)
                
    if key == ord('q'):
        # print(key)
        break