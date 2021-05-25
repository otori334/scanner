# http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html
# https://emotionexplorer.blog.fc2.com/blog-entry-181.html
# 罫線だけ消すやつ

import cv2
import sys
import numpy as np

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

img = cv2.imread(input_file_path, 0)

# 大雑把に罫線を消す
# この段階で消えてしまう横線と消えないノイズは現時点では以降の処理で解決できない
# この問題はハフ変換などの輪郭検出で克服できる可能性がある
kernel = np.ones((4, 1), np.uint8)
closing1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 文字領域を横に伸ばす
kernel = np.ones((10, 60), np.uint8)
erosion1 = cv2.erode(closing1, kernel, iterations = 1)

# 余白優先
or1 = cv2.bitwise_or(img, erosion1)

# 大雑把に罫線を消す
kernel = np.ones((3,1),np.uint8)
closing2 = cv2.morphologyEx(or1, cv2.MORPH_CLOSE, kernel)

# 文字のシルエットを大きくする
kernel = np.ones((7, 7), np.uint8)
erosion2 = cv2.erode(closing2, kernel, iterations = 1)

# 横伸びの文字領域と大きくした文字のシルエットが重複する領域を求める（余白優先で黒を足す）
bitwise = cv2.bitwise_or(erosion1, erosion2)

# 余白優先
or2 = cv2.bitwise_or(img, bitwise)

# 除いた罫線
# xor = cv2.bitwise_xor(img, or2)

"""
# cv2.imshow("xor", xor)
cv2.imshow("or2", or2)
cv2.imshow("bitwise", bitwise)
cv2.imshow("erosion2", erosion2)
cv2.imshow("closing2", closing2)
cv2.imshow("or1", or1)
cv2.imshow("erosion1", erosion1)
cv2.imshow("closing1", closing1)
cv2.imshow("img", img)
cv2.waitKey(0)
"""

cv2.imwrite(output_file_path, or2)
