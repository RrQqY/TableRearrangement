# CoppeliaSim Python 常用 API

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
