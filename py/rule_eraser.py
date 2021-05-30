# 罫線だけ消すやつ
import cv2
import sys
import numpy as np

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

# 罫線の歪みを吸収するROI領域の分割数
split_cols = 10

# 罫線の閾値
line_th = 3

img = cv2.imread(input_file_path, 0)
rows, cols = img.shape

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
len1 = cols // split_cols
len2 = len1 + 1
mod2 = cols % split_cols
mod1 = split_cols - mod2

# ブランク画像を作成
blank = np.zeros((rows, cols, 3), np.uint8)
blank = cv2.cvtColor(blank, cv2.COLOR_BGR2GRAY)

# 全ゼロデータに255を足してホワイトにする
blank += 255
line1 = blank.copy()

# https://kyudy.hatenablog.com/entry/2019/10/26/141330
thresh_spike = cols / line_th // split_cols
vp = {}
loc_y_spike = {}
for index in range(split_cols):
    vp[index] = np.sum((split_img[index] != 0).astype(np.uint8), axis=1)
    loc_y_spike[index] = np.where(vp[index] > thresh_spike)

# ブランク画像に線を描画する
x1 = split_cols_index = 0
for mod_index in range(mod2):
    x2 = x1 + len2
    for y in loc_y_spike[split_cols_index]:
        line1[y, x1:x2] = 0
    split_cols_index += 1
    x1 = x2
for mod_index in range(mod1):
    x2 = x1 + len1
    for y in loc_y_spike[split_cols_index]:
        line1[y, x1:x2] = 0
    split_cols_index += 1
    x1 = x2

# 線の歪みを考慮して線のシルエットを大きくする
kernel = np.ones((5,5),np.uint8)
line2 = cv2.erode(line1,kernel,iterations = 2)

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

# 白黒反転
line3 = 255 - line2

# 合成
bitwise2 = cv2.bitwise_or(closing3, erosion1)
bitwise3 = cv2.bitwise_or(img, line3)
bitwise4 = cv2.bitwise_and(bitwise2, bitwise3)

"""
cv2.imshow("bitwise5", bitwise5)
cv2.imshow("img", img)
cv2.waitKey(0)
"""

cv2.imwrite(output_file_path, bitwise4)
