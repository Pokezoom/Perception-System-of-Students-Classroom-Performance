# 前言

MTCNN，Multi-task convolutional neural network（多任务卷积神经网络），将人脸区域检测与人脸关键点检测放在了一起，总体可分为P-Net、R-Net、和O-Net三层网络结构。它是2016年中国科学院深圳研究院提出的用于人脸检测任务的多任务神经网络模型，该模型主要采用了三个级联的网络，采用候选框加分类器的思想，进行快速高效的人脸检测。这三个级联的网络分别是快速生成候选窗口的P-Net、进行高精度候选窗口过滤选择的R-Net和生成最终边界框与人脸关键点的O-Net。和很多处理图像问题的卷积神经网络模型，该模型也用到了图像金字塔、边框回归、非最大值抑制等技术。


# 环境
 - Pytorch 1.8.1
 - Python 3.7

# 文件介绍
 - `models/Loss.py` MTCNN所使用的损失函数，包括分类损失函数、人脸框损失函数、关键点损失函数
 - `models/PNet.py` PNet网络结构
 - `models/RNet.py` RNet网络结构
 - `models/ONet.py` ONet网络结构
 - `utils/data_format_converter.py` 把大量的图片合并成一个文件
 - `utils/data.py` 训练数据读取器
 - `utils/utils.py` 各种工具函数
 - `infer_path.py` 使用路径预测图像，检测图片上人脸的位置和关键的位置，并显示
 - `infer_camera.py` 预测图像程序，检测图片上人脸的位置和关键的位置实时显示
 - `infer_Video.py` 使用视频路径，识别视频中人脸box和关键点，并显示识别结果

# 预测

 - `python3 infer_path.py` 使用图像路径，识别图片中人脸box和关键点，并显示识别结果
   ![识别结果](D:\MTCNN\Pytorch-MTCNN-master\Multi_Face_Detection\dataset\path_test\test_result.png)

 - `python3 infer_camera.py` 使用相机捕获图像，识别图片中人脸box和关键点，并显示识别结果

 - `python3 infer_Video.py` 使用视频路径，识别视频中人脸box和关键点，并显示识别结果，创建一个face文件夹来存储当前秒的检测到的人脸图像，将视频拆分成帧并保存到path_to_save_frames文件夹，并生成一个带关键点和人脸框的视频

