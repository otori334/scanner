# 罫線だけ消すやつ
import cv2
import sys
import numpy as np

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

img = cv2.imread(input_file_path, 0)
rows, cols = img.shape

# 罫線の歪みを吸収するROI領域の分割数
split_cols = cols // 10

# 罫線の閾値
line_th1 = 4
line_th2 = 4

# 大雑把に罫線を消す
# http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html
kernel = np.ones((4, 1), np.uint8)
closing1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 除いた罫線
# https://emotionexplorer.blog.fc2.com/blog-entry-181.html
bitwise1 = cv2.bitwise_xor(img, closing1)

# 除いた罫線を縦に分割し線の歪みに対応する
split_img = {}
split_img = np.array_split(bitwise1, split_cols, 1)

# 分割した画像の剰余を考慮する
len2 = cols // split_cols
len1 = len2 + 1
mod1 = cols % split_cols
mod2 = split_cols - mod1

# https://kyudy.hatenablog.com/entry/2019/10/26/141330
thresh_spike = cols / line_th1 // split_cols
img_comp1 = np.zeros((split_cols, rows), np.uint8)
loc_y_spike = {}
for index in range(split_cols):
    img_comp1[index, np.where(np.sum((split_img[index] != 0).astype(np.uint8), axis=1) > thresh_spike)] = 255

# 線を描画する
img_comp1_1, img_comp1_2 = np.split(img_comp1, [mod1], 0)
line1 = np.block([[img_comp1_1.repeat(len1,axis=0)], [img_comp1_2.repeat(len2,axis=0)]]).T

# 大雑把に罫線を消す
kernel = np.ones((4,1),np.uint8)
closing2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 黒をつなげる
kernel = np.ones((20, 200), np.uint8) 
opening1 = cv2.morphologyEx(closing2, cv2.MORPH_OPEN, kernel)

# 黒を太くする
kernel = np.ones((10,10),np.uint8)
erosion1 = cv2.erode(opening1, kernel, iterations = 1)

# 大雑把に罫線を消す
kernel = np.ones((3,1),np.uint8)
closing3 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 合成
bitwise3 = cv2.bitwise_or(closing3, erosion1)
bitwise4 = cv2.bitwise_or(img, line1)
bitwise5 = cv2.bitwise_and(bitwise3, bitwise4)

"""
cv2.imshow("bitwise5", bitwise5); cv2.waitKey(0); quit()
cv2.imshow("img", img)
cv2.waitKey(0)
"""

cv2.imwrite(output_file_path, bitwise5)
