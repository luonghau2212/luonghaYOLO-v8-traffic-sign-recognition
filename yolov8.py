# -*- coding: utf-8 -*-
"""yolov8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yP1waO--WS5nbnhWkO2dz7G-XYeUSn31
"""

from google.colab import drive
drive.mount('/content/drive')

cd /content/drive/MyDrive/yolov8

ls

pip install ultralytics

from ultralytics import YOLO

model = YOLO("yolov8x.pt")

results = model.train(data="/content/drive/MyDrive/yolov8/via-trafficsign/via-trafficsign.yaml", epochs=8, batch=4)

from ultralytics import YOLO
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

model = YOLO("/content/drive/MyDrive/yolov8/runs/detect/train2/weights/best.pt")
results = model("/content/drive/MyDrive/yolov8/00007.jpg")

# Duyệt qua các kết quả dự đoán
for r in results:
    # Vẽ kết quả dự đoán lên hình ảnh
    im_array = r.plot()
    im_array_rgb = im_array[..., ::-1]  # Đảo ngược kênh màu từ BGR sang RGB
    # Hiển thị hình ảnh
    plt.imshow(im_array_rgb)
    plt.axis('off')
    plt.show()

model = YOLO("/content/drive/MyDrive/yolov8/runs/detect/train2/weights/best.pt")
results = model("/content/drive/MyDrive/yolov8/00030.jpg")

# Duyệt qua các kết quả dự đoán
for r in results:
    # Vẽ kết quả dự đoán lên hình ảnh
    im_array = r.plot()
    im_array_rgb = im_array[..., ::-1]  # Đảo ngược kênh màu từ BGR sang RGB
    # Hiển thị hình ảnh
    plt.imshow(im_array_rgb)
    plt.axis('off')
    plt.show()

