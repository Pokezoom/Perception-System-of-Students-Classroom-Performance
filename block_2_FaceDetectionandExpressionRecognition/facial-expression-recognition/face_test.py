import os
import cv2
import numpy as np
import tensorflow as tf
from collections import Counter
# 加载模型
model = tf.keras.models.load_model('network-5Labels.h5')
labels = ['Surprise', 'Neutral', 'Anger', 'Happy', 'Sad']

# 用来存储所有预测结果的字典
predictions_dict = {}

# 构建桌面路径
base_path = "/users/pengkezhong/Desktop/face/"

# 确保路径是正确的
if not os.path.exists(base_path):
    raise Exception(f"The path {base_path} does not exist.")

# 遍历 base_path 下的所有文件夹
for folder in sorted(os.listdir(base_path)):
    folder_path = os.path.join(base_path, folder)
    if os.path.isdir(folder_path):
        predictions_dict[folder] = []

        # 遍历当前文件夹内的所有图片
        for image_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_name)
            if os.path.isfile(image_path) and image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                img = cv2.imread(image_path)
                if img is not None:
                    # 由于我们知道图片中只有单个人脸，我们可以直接缩放图片
                    face = cv2.resize(img, (48, 48))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    face = face / 255.0
                    prediction = model.predict(np.array([face.reshape((48, 48, 1))])).argmax()
                    state = labels[prediction]
                    predictions_dict[folder].append((image_name, state))
                else:
                    print(f"Failed to read image {image_name}.")
            else:
                print(f"Skipped file {image_name}, not an image.")

# 输出结果
# for second, results in predictions_dict.items():
#     print(f"Results for {second}: {results}")

# 用于存储每个文件夹中每个表情的计数的字典
expressions_count = {}

for folder, results in predictions_dict.items():
    # 使用Counter来计算每个表情的数量
    count = Counter([expression for _, expression in results])
    expressions_count[folder] = dict(count)

# 打印每个文件夹的表情计数结果
for folder, counts in expressions_count.items():
    print(f"Counts for {folder}: {counts}")
