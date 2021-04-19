import sys
import cv2

input_file_path = sys.argv[1]
output_file_path = input_file_path

img = cv2.imread(input_file_path)
rows,cols,channels = img.shape
frame = 0
color = (255, 255, 255)
cv2.rectangle(img, (frame, frame), (cols - frame, rows - frame), color, thickness=15)
cv2.rectangle(img, (0, round(rows * 0.965)), (cols, rows), color, thickness=-1)
cv2.rectangle(img, (0, 0), (cols, round(rows * 0.02)), color, thickness=-1)

cv2.imwrite(output_file_path, img)
