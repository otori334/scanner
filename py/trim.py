import cv2
import sys
import numpy as np

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

img = cv2.imread(input_file_path)

rows,cols,channels = img.shape

# 左上
a = np.array([230, 175])
# 右下
b = np.array([2505, 1880])
img1 = img[a[1] : b[1], a[0]: b[0]]

# img[top : bottom, left : right]
#img1 = img[255 : 1790, 0: cols]

cv2.imwrite(output_file_path, img1)
