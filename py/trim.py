import cv2
import sys
import numpy as np

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

img = cv2.imread(input_file_path)

# 左上
a = np.array([230, 175])
# 右下
b = np.array([2505, 1880])
img1 = img[a[1] : b[1], a[0]: b[0]]

# img[top : bottom, left : right]
#img1 = img[175 : 1875, 230: 2505]

cv2.imwrite(output_file_path, img1)
