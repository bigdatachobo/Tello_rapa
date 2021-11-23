from move_control import keyboard_control
from simple_streaming import tello_video
from djitellopy import Tello

tello = Tello()
tello.connect()

# 패널
tello.streamon()

keyboard_control()
tello_video()