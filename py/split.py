# 分割するやつ
import cv2
import sys
import numpy as np

input_file_path = sys.argv[1]
output_file_path0 = sys.argv[2]
output_file_path1 = sys.argv[3]

img = cv2.imread(input_file_path, 0)

split_img = np.array_split(img, 2, 0) # 0:横長ふたつ, 1:縦長ふたつ

cv2.imwrite(output_file_path0, split_img[0])
cv2.imwrite(output_file_path1, split_img[1])
