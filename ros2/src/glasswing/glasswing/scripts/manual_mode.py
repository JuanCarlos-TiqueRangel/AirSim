# use open cv to show new images from AirSim 
import setup_path 
import airsim

# requires Python 3.5.3 :: Anaconda 4.4.0
# pip install opencv-python
import cv2
import time
import math
import sys
import numpy as np

client = airsim.MultirotorClient()

client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)
client.takeoffAsync().join()

while True:
    key = airsim.wait_key()
    vx = 0
    vy = 0
    vz = 0
    yaw = 0

    print("key_value: ", key)

    """
    if key == 'w':
        vx = 1.0
    if key == 's':
        vx = -1.0
    if key == 'd':
        vy = 0.1
    if key == 'a':
        vy = -0.1
    if key == 'i':
        vz = -0.05
    if key == 'k':
        vz = 0.05
    if key == 'l':
        yaw = 5
    if key == 'j':
        yaw = -5
    """

    if key == 'w':
        vx = 1.0
    if key == 's':
        vx = -1.0
    if key == 'd':
        vy = 1.0
    if key == 'a':
        vy = -1.0
    if key == 'i':
        vz = -0.05
    if key == 'k':
        vz = 0.05
    if key == 'l':
        yaw = 1
    if key == 'j':
        yaw = -1    

    client.moveByVelocityAsync(vx, vy, vz, 70, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(True, yaw)).join()
    #client.moveByRollPitchYawZAsync(0, 0, yaw, None, 200).join()
