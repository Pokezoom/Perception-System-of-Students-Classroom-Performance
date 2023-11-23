# Perception-System-of-Students-Classroom-Performance
模块一：多目标人脸检测、
模块二：课堂表情识别、
模块三：疲劳状态检测、
模块四：头部姿态估计、
模块五：身体倾斜度检测、
模块六：用模糊综合评价算法代入模块2-5测到的数据计算学生注意力

![./README.assets/image-20230724183025706.png)



web.py文件是用fastAPI搭建的一个服务，主要是暴露各个模块的接口。

下载fastapi框架包

```
pip install fastapi
pip install uvicorn[standard]
pip install python-multipart
```

启动方法：

```
uvicorn web:app --reload
```

