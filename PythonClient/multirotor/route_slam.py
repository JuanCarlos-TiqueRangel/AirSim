import setup_path
import airsim

import numpy as np
import os
import tempfile
import pprint
import cv2

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

state = client.getMultirotorState()
s = pprint.pformat(state)
print("state: %s" % s)

imu_data = client.getImuData()
s = pprint.pformat(imu_data)
print("imu_data: %s" % s)

barometer_data = client.getBarometerData()
s = pprint.pformat(barometer_data)
print("barometer_data: %s" % s)

magnetometer_data = client.getMagnetometerData()
s = pprint.pformat(magnetometer_data)
print("magnetometer_data: %s" % s)

gps_data = client.getGpsData()
s = pprint.pformat(gps_data)
print("gps_data: %s" % s)

airsim.wait_key('Press any key to takeoff')
print("Taking off...")
client.armDisarm(True)
client.takeoffAsync().join()

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

airsim.wait_key('Press any key to move vehicle to (-10, 10, -10) at 5 m/s')
#client.moveToPositionAsync(-10, 10, -10, 5).join()
client.moveToPositionAsync(0, 10, -1, 0.5).join()
client.landAsync().join()

client.armDisarm(True)
client.takeoffAsync().join()
client.moveToPositionAsync(0, 15, -1, 0.5).join()
client.landAsync().join()

client.armDisarm(True)
client.takeoffAsync().join()
client.moveToPositionAsync(0, 20, -1, 0.5).join()
client.landAsync().join()

client.armDisarm(True)
client.takeoffAsync().join()
client.moveToPositionAsync(0, 25, -1, 0.5).join()
client.landAsync().join()

#client.hoverAsync().join()

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

airsim.wait_key('Press any key to reset to original state')

client.reset()
client.armDisarm(False)

# that's enough fun for now. let's quit cleanly
client.enableApiControl(False)
