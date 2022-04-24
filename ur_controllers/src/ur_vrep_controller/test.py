import b0RemoteApi
import time
 
 
with b0RemoteApi.RemoteApiClient('节点名称', '通道名字') as client:
    client.doNextStep = True
 
    def simulationStepStarted(msg):
        simTime = msg[1][b'simulationTime']
 
    def simulationStepDone(msg):
        simTime = msg[1][b'simulationTime']
        client.doNextStep = True
 
    client.simxSynchronous(True)
    client.simxGetSimulationStepStarted(client.simxDefaultSubscriber(simulationStepStarted))
    client.simxGetSimulationStepDone(client.simxDefaultSubscriber(simulationStepDone))
    client.simxStartSimulation(client.simxDefaultPublisher())  # 开始仿真
    startTime = time.time()
    while time.time() < startTime + 40:   # 仿真时间设定
        if client.doNextStep:
            client.doNextStep = False
            '''控制代码'''
            client.simxSynchronousTrigger()
        client.simxSpinOnce()
    client.simxStopSimulation(client.simxDefaultPublisher())  # 结束仿真
