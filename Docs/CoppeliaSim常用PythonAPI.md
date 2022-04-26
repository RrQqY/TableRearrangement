## CoppeliaSim Python 常用 API

### simxGetJointPosition

检索关节的固有位置

```python
number returnCode,number position=simxGetJointPosition(number clientID,number jointHandle,number operationMode) 
```

- 参数：
  - clientID：客户端ID
  - jointHandle：关节句柄
  - operaMode：远程API函数操作模式，此函数的推荐操作模式是 simx_opmode_blocking  
- 返回值：
  - returnCode：远程API函数返回码
  - position：关节位置



### simxGetObjectHandle

根据路径和别名检索对象句柄

```python
number returnCode,number handle=simxGetObjectHandle(number clientID,string objectPath,number operationMode)
```

- 参数：
  - clientID：客户端ID
  - objectPath：对象路径（名称）
  - operaMode：远程API函数操作模式，此函数的推荐操作模式是 simx_opmode_blocking  
- 返回值：
  - returnCode：远程API函数返回码
  - handle：对象句柄



### simxGetObjectPosition 

检索对象的位置

```python
number returnCode, array position=simxGetObjectPosition(number clientID,number objectHandle,number relativeToObjectHandle,number operationMode) 
```

- 参数：
  - clientID：客户端ID
  - objectHandle：对象句柄
  - relativeToObjectHandle：指示相对于我们想要的位置的参考框架。 指定 -1 检索绝对位置，sim_handle_parent 检索相对于对象父级的位置，或相对于您想要该位置的参考框架的对象句柄
  - operaMode：远程API函数操作模式，此函数的推荐操作模式是 simx_opmode_blocking  
- 返回值：
  - returnCode：远程API函数返回码
  - position：位置（x, y, z）



### simxGetObjectQuaternion 

检索对象的四元数

```python
number returnCode,array quat=simxGetObjectQuaternion(number clientID,number objectHandle,number relativeToObjectHandle,number operationMode) 
```

- 参数：
  - clientID：客户端ID
  - objectHandle：对象句柄
  - relativeToObjectHandle：指示相对于我们想要的四元数的参考框架。 指定 -1 检索绝对位置，sim_handle_parent 检索相对于对象父级的位置，或相对于您想要该位置的参考框架的对象句柄
  - operaMode：远程API函数操作模式，此函数的推荐操作模式是 simx_opmode_blocking  
- 返回值：
  - returnCode：远程API函数返回码
  - quat：四元数 (x, y, z, w) 



### simxGetObjectVelocity 

检索对象的线速度和角速度

```python
number returnCode, array linearVelocity, array angularVelocity=simxGetObjectVelocity(number clientID,number objectHandle,number operationMode) 
```

- 参数：
  - clientID：客户端ID
  - objectHandle：对象句柄
  - operaMode：远程API函数操作模式，此函数的推荐操作模式是 simx_opmode_blocking  
- 返回值：
  - returnCode：远程API函数返回码
  - linearVelocity：线速度 (vx, vy, vz) 
  - angularVelocity：角速度 (dAlpha, dBeta, dGamma) 



### simxGetVisionSensorImage 

检索视觉传感器的图像

```python
number returnCode,array resolution,array image=simxGetVisionSensorImage(number clientID,number sensorHandle,number options,number operationMode) 
```

- 参数：
  - clientID：客户端ID
  - sensorHandle：视觉传感器句柄
  - options：选项，bit0则每个图像像素是一个字节（灰度图像），否则每个图像像素是一个 rgb byte-triplet 
  - operaMode：远程API函数操作模式，此函数的推荐操作模式是 simx_opmode_blocking  
- 返回值：
  - returnCode：远程API函数返回码
  - resolution：图像的分辨率（x, y）
  - image：图像数据。



### simxGetVisionSensorDepthBuffer 

检索视觉传感器的深度缓冲区

```python
number returnCode,array resolution,array buffer=simxGetVisionSensorDepthBuffer(number clientID,number sensorHandle,number operationMode) 
```

- 参数：
  - clientID：客户端ID
  - sensorHandle：视觉传感器句柄
  - operaMode：远程API函数操作模式，此函数的推荐操作模式是 simx_opmode_blocking  
- 返回值：
  - returnCode：远程API函数返回码
  - resolution：图像的分辨率（x, y）
  - buffer：深度缓冲区数据。值在 0-1的范围内（0=离传感器最近，1=离传感器最远）



### simxLoadModel 

加载以前保存的模型

```python
number returnCode,number baseHandle=simxLoadModel(number clientID,string modelPathAndName,number options,number operationMode) 
```

- 参数：
  - clientID：客户端ID
  - modelPathAndName：模型文件名，包括路径和扩展名（“ttm”）
  - options：选项，bit0则指定文件位于客户端
  - operaMode：远程API函数操作模式，此函数的推荐操作模式是 simx_opmode_blocking  
- 返回值：
  - returnCode：远程API函数返回码
  - baseHandle：加载的模型库。 



### simxLoadScene 

加载以前保存的场景

```python
number returnCode=simxLoadScene(number clientID,string scenePathAndName,number options,number operationMode) 
```

- 参数：
  - clientID：客户端ID
  - scenePathAndName：场景文件名，包括路径和扩展名（“ttt”）
  - options：选项，bit0则指定文件位于客户端
  - operaMode：远程API函数操作模式，此函数的推荐操作模式是 simx_opmode_blocking  
- 返回值：
  - returnCode：远程API函数返回码



### simxSetJointTargetPosition

如果关节处于扭矩/力模式，设置关节的目标位置

```python
number returnCode=simxSetJointPosition(number clientID,number jointHandle,number position,number operationMode) 
```

- 参数：
  - clientID：客户端ID
  - jointHandle：关节句柄
  - position：关节位置
  - operaMode：远程API函数操作模式，此函数的推荐操作模式是 simx_opmode_blocking  
- 返回值：
  - returnCode：远程API函数返回码



### simxSetObjectPosition 

设置对象的位置

```python
number returnCode=simxSetObjectPosition(number clientID,number objectHandle,number relativeToObjectHandle,array position,number operationMode) 
```

- 参数：
  - clientID：客户端ID
  - objectHandle：对象句柄
  - relativeToObjectHandle：指示相对于我们想要的位置的参考框架。 指定 -1 检索绝对位置，sim_handle_parent 检索相对于对象父级的位置，或相对于您想要该位置的参考框架的对象句柄
  - position：位置（x, y, z）
  - operaMode：远程API函数操作模式，此函数的推荐操作模式是 simx_opmode_blocking  
- 返回值：
  - returnCode：远程API函数返回码



### simxSetObjectOrientation 

设置对象的方向（ 欧拉角 ）

```python
number returnCode=simxSetObjectOrientation(number clientID,number objectHandle,number relativeToObjectHandle,array eulerAngles,number operationMode) 
```

- 参数：
  - clientID：客户端ID
  - objectHandle：对象句柄
  - relativeToObjectHandle：指示相对于我们想要的位置的参考框架。 指定 -1 检索绝对位置，sim_handle_parent 检索相对于对象父级的位置，或相对于您想要该位置的参考框架的对象句柄
  - eulerAngles：欧拉角（α，β和γ） 
  - operaMode：远程API函数操作模式，此函数的推荐操作模式是 simx_opmode_blocking  
- 返回值：
  - returnCode：远程API函数返回码



## CoppeliaSim 相关网站

- CoppeliaSim Edu V4.1.0 + Ubuntu 16.04 + ROS Kinetic环境搭建与基础测试

  https://www.freesion.com/article/81111354822/

- Vrep与Python实现联合控制的通讯问题

  https://wenku.baidu.com/view/5f87e52ff48a6529647d27284b73f242336c31f1.html

- Coppeliasim与python的联动——The B0-based remote API

  https://blog.csdn.net/qq_42286607/article/details/116862594

- CoppeliaSim(原V-REP)新手上路

  https://blog.csdn.net/qq_37051669/article/details/115324851

- 官网[Remote API](https://www.coppeliarobotics.com/helpFiles/en/remoteApiOverview.htm) functions (Python)

  https://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm

- js image 获取rgb_VREP 获取 RGB / Depth 图（Python API）

  https://blog.csdn.net/weixin_39572409/article/details/110745852

- 使用Python对UR5进行轨迹规划

  https://www.guyuehome.com/35685

- 保姆级教学——虚拟机器人平台vrep(coppeliaSim)的机器人平台搭建

  https://blog.csdn.net/qq_39243015/article/details/106247956?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_paycolumn_v3&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_paycolumn_v3&utm_relevant_index=1

- 用UR5进行识别、抓取和码垛

  https://blog.csdn.net/uuuuur/article/details/108028900
