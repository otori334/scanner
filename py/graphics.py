import sys
import cv2

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

img = cv2.imread(input_file_path)
rows,cols,channels = img.shape
frame = 60
color = (255, 255, 255)

#cv2.rectangle(img, (frame, frame), (cols - frame, rows - frame), color, thickness=15)
# 一番下を白くする
cv2.rectangle(img, (0, round(rows * 0.99)), (cols, rows), color, thickness=-1)

# 一番上を白くする
cv2.rectangle(img, (0, 0), (cols, round(rows * 0.02)), color, thickness=-1)

# 一番左を白くする
cv2.rectangle(img, (0, 0), (round(cols * 0.05), rows), color, thickness=-1)

# 一番右を白くする
cv2.rectangle(img, (round(cols * 0.95), 0), (cols, rows), color, thickness=-1)

# 左上を白くする
#cv2.rectangle(img, (0, 0), (950, 297), color, thickness=-1)

cv2.imwrite(output_file_path, img)
