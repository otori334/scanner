# 傾けるやつ
import cv2
import sys
import numpy as np

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]
angle = float(sys.argv[3]) # 時計回りに回転角を指定

img = cv2.imread(input_file_path, 0)

height, width = img.shape
center = (int(width/2), int(height/2))

scale = 1.0
trans = cv2.getRotationMatrix2D(center, angle , scale)
image2 = cv2.warpAffine(img, trans, (width,height), borderValue=255) # 白い背景

cv2.imwrite(output_file_path, image2)
