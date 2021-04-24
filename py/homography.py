# https://www.omoshiro-suugaku.com/entry/mouse-position # <-遅い
# https://techacademy.jp/magazine/51035 # <-速い
# https://self-development.info/opencvによる台形補正・射影変換を解説【python】/
import cv2
import numpy as np
import math
import sys

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

plist=[]

img = cv2.imread(input_file_path , cv2.IMREAD_COLOR)
window_name = 'img'

def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        plist.append([x, y])
        #print("{}, {}".format(x, y))

cv2.imshow(window_name, img)
cv2.setMouseCallback(window_name, onMouse)

cv2.waitKey(0)

# 比率調整
w_ratio = 1

# 変換前4点の座標　p1:左上　p2:右上 p3:左下 p4:左下
p1 = np.array(plist[0])
p2 = np.array(plist[1])
p3 = np.array(plist[2])
p4 = np.array(plist[3])

# 入力画像の読み込み
img = cv2.imread(input_file_path)
 
#　幅取得
o_width = np.linalg.norm(p2 - p1)
o_width = math.floor(o_width * w_ratio)
 
#　高さ取得
o_height = np.linalg.norm(p3 - p1)
o_height = math.floor(o_height)
 
# 変換前の4点
src = np.float32([p1, p2, p3, p4])
 
# 変換後の4点
dst = np.float32([[0, 0],[o_width, 0],[0, o_height],[o_width, o_height]])
 
# 変換行列
M = cv2.getPerspectiveTransform(src, dst)
 
# 射影変換・透視変換する
output = cv2.warpPerspective(img, M,(o_width, o_height))
 
# 射影変換・透視変換した画像の保存
cv2.imwrite(output_file_path, output)
