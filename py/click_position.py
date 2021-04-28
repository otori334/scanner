# https://techacademy.jp/magazine/51035
import cv2
import sys

input_file_path = sys.argv[1]

img = cv2.imread(input_file_path , cv2.IMREAD_COLOR)
window_name = 'img'

def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("{}, {}".format(x, y))

cv2.imshow(window_name, img)
cv2.setMouseCallback(window_name, onMouse)
cv2.waitKey(0)
