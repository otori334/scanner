# https://qiita.com/fallaf/items/1c5387a79027b2ec64b0
import sys
import cv2
import numpy as np

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

img = cv2.imread(input_file_path)
ksize = 51
blur = cv2.blur(img, (ksize, ksize))

# 0徐算が起きても後の処理によりnanはなくなるので警告を消すだけに留めた
# https://teratail.com/questions/190718
np.seterr(divide='ignore', invalid='ignore')

rij = img/blur
index_1 = np.where(rij >= 1.00) # 1以上の値があると邪魔なため
rij[index_1] = 1
rij_int = np.array(rij*255, np.uint8) # 除算結果が実数値になるため整数に変換
rij_HSV = cv2.cvtColor(rij_int, cv2.COLOR_BGR2HSV)
ret, thresh = cv2.threshold(rij_HSV[:,:,2], 0, 255, cv2.THRESH_OTSU)
rij_HSV[:,:,2] = thresh
rij_ret = cv2.cvtColor(rij_HSV, cv2.COLOR_HSV2BGR)
cv2.imwrite(output_file_path, rij_ret)
