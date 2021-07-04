# 分割するやつ2
import cv2
import sys
import numpy as np

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]
swap = int(sys.argv[3])

img = cv2.imread(input_file_path, 0)

L = img[:,:swap]
R = img[:,swap:]
RL = cv2.hconcat([R, L])

cv2.imwrite(output_file_path, RL)
