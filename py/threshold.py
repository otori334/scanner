# https://qiita.com/tokkuri/items/ad5e858cbff8159829e9
import sys
import cv2

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

img = cv2.imread(input_file_path, 0)

# 閾値の設定
threshold = 100

# 二値化(閾値100を超えた画素を255にする。)
ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

cv2.imwrite(output_file_path, img_thresh)
