import sim
import time
import math
import numpy as np
import cv2
import matplotlib.pyplot as mpl

sim.simxFinish(-1)    # just in case, close all opened connections
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)    # Connect to CoppeliaSim


if clientID != -1:
    print ('Connected to remote API server')

    #-------------------------------- start--初始化部分 --------------------------------#
    ret, URhandle1 = sim.simxGetObjectHandle(clientID, 'UR5_joint1', 
                     sim.simx_opmode_blocking)
    ret, URhandle2 = sim.simxGetObjectHandle(clientID, 'UR5_joint2', 
                     sim.simx_opmode_blocking)
    ret, URhandle3 = sim.simxGetObjectHandle(clientID, 'UR5_joint3', 
                     sim.simx_opmode_blocking)
    ret, URhandle4 = sim.simxGetObjectHandle(clientID, 'UR5_joint4', 
                     sim.simx_opmode_blocking)
    ret, URhandle5 = sim.simxGetObjectHandle(clientID, 'UR5_joint5', 
                     sim.simx_opmode_blocking)
    ret, URhandle6 = sim.simxGetObjectHandle(clientID, 'UR5_joint6', 
                     sim.simx_opmode_blocking)
    ret, KinectRGBAbovehandle = sim.simxGetObjectHandle(clientID, 'kinect_rgb_above', 
                     sim.simx_opmode_blocking)
    ret, KinectDepthAbovehandle = sim.simxGetObjectHandle(clientID, 'kinect_depth_above', 
                     sim.simx_opmode_blocking)
    ret, KinectRGBhandle = sim.simxGetObjectHandle(clientID, 'kinect_rgb', 
                     sim.simx_opmode_blocking)
    ret, KinectDepthhandle = sim.simxGetObjectHandle(clientID, 'kinect_depth', 
                     sim.simx_opmode_blocking)

    #-------------------------------- end--初始化部分 --------------------------------#

    #-------------------------------- start--主程序部分 --------------------------------#
    # 测试控制机械臂关节角度，并读取角度值
    ret = sim.simxSetJointTargetPosition(clientID, URhandle1, np.pi, sim.simx_opmode_blocking)
    ret,  position1 = sim.simxGetJointPosition(clientID, URhandle1, sim.simx_opmode_blocking)
    print(position1)
    
    targetPos = (-0.022, -0.340, 0.75)
    sim_ret, UR5_target_handle = sim.simxGetObjectHandle(clientID, 'UR5_Target', sim.simx_opmode_blocking)
    sim.simxSetObjectPosition(clientID, UR5_target_handle, -1, targetPos, sim.simx_opmode_blocking)

    #-------------------------------- end--主程序部分 --------------------------------#
else:
    print ('Failed connecting to remote API server')
