import cv2
import sys
import numpy as np

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

img = cv2.imread(input_file_path)

# 膨張と組み合わせたら罫線を除いた文字領域を取得できそう
kernel = np.ones((4,1),np.uint8)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imwrite(output_file_path, closing)
