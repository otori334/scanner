import cv2
import sys

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

img = cv2.imread(input_file_path)

# img[top : bottom, left : right]
img1 = img[175 : 1875, 230: 2505]

cv2.imwrite(output_file_path, img1)
