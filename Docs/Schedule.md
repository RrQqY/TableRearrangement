# 项目进度安排

2022年3月-6月：ROS、机器学习等理论学习，继续查阅相关文献资料，整理知识框架，细化工作流程；项目环境的搭建，初步实现机械臂运动控制及深度相机信息获取；

2022年7月-8月：结合深度相机信息对目标物体建模，实现物体数据获取系统；

2022年9月-10月：分析机械臂感知的信息增益并进行模型训练，实现主动感知和交互感知；

2022年11月-12月：对机械臂进行运动学建模，分析其动作代价并进行模型训练，实现机械臂运动轨迹最优规划；

2022年12月-结题：总结完善项目内容并优化，完成论文。

| 时间            | 事件                                                         | 具体内容                    |
| --------------- | :----------------------------------------------------------- | --------------------------- |
| 22.03末-22.05末 | 搭建项目环境（ROS包搭建、机械臂建模），做出IO接口（包括机械臂运动控制、深度相机信息获取） | Ubuntu、ROS、Python，Moveit |
| 22.05末-22.07中 | 物体数据获取系统的实现（FCN语义分割，基于RGB-D图和点云实现物体轮廓建模和位姿、完整度获取） | 机器视觉（OpenCV）          |
| 22.07中-22.11末 | 主动感知、交互感知的实现（强化学习）                         |                             |
| 22.11末-23.01末 | 物体特征获取和比对（KNN），运动规划（深度学习）              |                             |
| 23.01末-结题    | 优化+成果完成                                                |                             |
