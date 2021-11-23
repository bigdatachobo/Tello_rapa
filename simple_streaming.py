from djitellopy import Tello
import cv2 as cv

# tello 생성자 생성
tello = Tello()

# tello 연결
tello.connect()

# 멀티 쓰레드로 작동함
# 조종 쓰레드와 비디오 쓰레드가 따로 되어있음.
# tello video 연결

tello.streamon()

# 비디오 연결
def tello_video():
    while True:
        fr_read = tello.get_frame_read()
        cv.imshow('tello stream', fr_read.frame)
        cv.waitKey(1)
            
# tello video 끄기    
# tello.streamoff()
