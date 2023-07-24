import cv2
from mtcnn import MTCNN
import os

# 读视频
cap = cv2.VideoCapture('6_1690187711.mp4')
detector = MTCNN()

# 存图片的地方
if not os.path.exists('faces'):
    os.makedirs('faces')

i = 0
face_count = 0
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == False:
        break

    # 每隔10帧（即0.3秒，假设视频是30fps）检测一次人脸
    if i % 10 == 0:
        # 进行人脸检测
        result = detector.detect_faces(frame)
        for person in result:
            bounding_box = person['box']
            keypoints = person['keypoints']

            cv2.rectangle(frame,
                          (bounding_box[0], bounding_box[1]),
                          (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                          (0,155,255),
                          2)

            # 保存人脸图片
            roi_gray = frame[bounding_box[1]:bounding_box[1] + bounding_box[3], bounding_box[0]:bounding_box[0] + bounding_box[2]]
            cv2.imwrite('faces/face_' + str(face_count) + '.jpg', roi_gray)
            face_count += 1

        # 显示结果
        cv2.imshow('frame',frame)

    i += 1

cap.release()
cv2.destroyAllWindows()
