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
    ret = sim.simxSetJointTargetPosition(clientID, URhandle1, np.pi,
                      sim.simx_opmode_blocking)
    ret,  position1 = sim.simxGetJointPosition(clientID, URhandle1, 
                      sim.simx_opmode_blocking)
    print(position1)

    while True:
        ## 获取上空Kinect相机的RGB图像
        ret, AboveRGBResolution, AboveRGBImage = sim.simxGetVisionSensorImage(clientID,
                            KinectRGBAbovehandle, 0, sim.simx_opmode_blocking) 
        ## 获取上空Kinect相机的深度图像，范围0~1
        ret, AboveDepthResolution, AboveDepthImage = sim.simxGetVisionSensorDepthBuffer(clientID,
                            KinectDepthAbovehandle, sim.simx_opmode_blocking) 
        ## 获取机械臂Kinect相机的RGB图像
        ret, RGBResolution, RGBImage = sim.simxGetVisionSensorImage(clientID,
                            KinectRGBhandle, 0, sim.simx_opmode_blocking) 
        ## 获取机械臂Kinect相机的深度图像，范围0~1
        ret, DepthResolution, DepthImage = sim.simxGetVisionSensorDepthBuffer(clientID,
                            KinectDepthhandle, sim.simx_opmode_blocking) 

        ## 预处理上空Kinect相机的RGB图像
        AboveRGBImage.reverse()
        sensorImage0 = np.array(AboveRGBImage, dtype = np.uint8)
        sensorImage0.resize([AboveRGBResolution[1], AboveRGBResolution[0], 3])
        sensorImage0 = cv2.flip(sensorImage0,1,dst=None)    # 左右翻转
        
        ## 预处理上空Kinect相机的深度图像
        AboveDepthImage.reverse()
        sensorImage1 = np.array(AboveDepthImage, dtype = np.float32)
        sensorImage1.resize([AboveDepthResolution[1], AboveDepthResolution[0]])
        sensorImage1 = cv2.flip(sensorImage1,1,dst=None)
        smax = sensorImage1.max()
        smin = sensorImage1.min()
        #归一化显示
        for i in range(AboveDepthResolution[1]):
            for j in range(AboveDepthResolution[0]):
                sensorImage1[i][j] =  sensorImage1[i][j] * (smax - smin) + smin

        ## 预处理机械臂Kinect相机的RGB图像
        RGBImage.reverse()
        sensorImage2 = np.array(RGBImage, dtype = np.uint8)
        sensorImage2.resize([RGBResolution[1], RGBResolution[0], 3])
        sensorImage2 = cv2.flip(sensorImage2,1,dst=None)    # 左右翻转
        
        ## 预处理机械臂Kinect相机的深度图像
        DepthImage.reverse()
        sensorImage3 = np.array(DepthImage, dtype = np.float32)
        sensorImage3.resize([DepthResolution[1], DepthResolution[0]])
        sensorImage3 = cv2.flip(sensorImage3,1,dst=None)
        smax = sensorImage3.max()
        smin = sensorImage3.min()
        #归一化显示
        for i in range(DepthResolution[1]):
            for j in range(DepthResolution[0]):
                sensorImage3[i][j] =  sensorImage3[i][j] * (smax - smin) + smin

        cv2.imshow("AboveRGB", sensorImage0)
        cv2.imshow("AboveDepth", sensorImage1)
        cv2.imshow("RGB", sensorImage2)
        cv2.imshow("Depth", sensorImage3)
        cv2.waitKey(1)


    #-------------------------------- end--主程序部分 --------------------------------#
else:
    print ('Failed connecting to remote API server')