# https://www.omoshiro-suugaku.com/entry/mouse-position # <-遅い
# https://techacademy.jp/magazine/51035 # <-速い
# https://qiita.com/otakoma/items/04e525ac74b7191dffe6 # テニスコート領域
# https://self-development.info/opencvによる台形補正・射影変換を解説【python】/
import cv2
import numpy as np
import math
import sys

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]


class PointList():
    def __init__(self, npoints):
        self.npoints = npoints
        self.ptlist = np.empty((npoints, 2), dtype=int)
        self.pos = 0

    def add(self, x, y, h):
        if self.pos != 0:
            for num in range(self.pos):
                a = np.array([x, y])
                if np.linalg.norm(self.ptlist[num, :] - a) < round(h * 0.1):
                    self.ptlist[num, :] = [x, y]
                    return True
            
        if self.pos < self.npoints:
            self.ptlist[self.pos, :] = [x, y]
            self.pos += 1
            return True
        return False


def onMouse(event, x, y, flag, params):
    wname, img, ptlist, h, w = params
    if event == cv2.EVENT_MOUSEMOVE:  # マウスが移動したときにx線とy線を更新する
        img2 = np.copy(img)
        cv2.line(img2, (x, 0), (x, h - 1), (255, 0, 0))
        cv2.line(img2, (0, y), (w - 1, y), (255, 0, 0))
        
        if ptlist.pos != 0:
            for num in range(ptlist.pos):
                cv2.drawMarker(img2, (ptlist.ptlist[num][0], ptlist.ptlist[num][1]), (0, 255, 0), markerSize=round(h * 0.1), thickness=3)
                cv2.circle(img2, (ptlist.ptlist[num][0], ptlist.ptlist[num][1]), round(h * 0.05), (255, 0, 0), thickness=3)
        
        cv2.imshow(wname, img2)

    if event == cv2.EVENT_LBUTTONDOWN:  # レフトボタンをクリックしたとき、ptlist配列にx,y座標を格納する
        if ptlist.add(x, y, h):
            img2 = np.copy(img)
            
            if ptlist.pos != 0:
                for num in range(ptlist.pos):
                    cv2.drawMarker(img2, (ptlist.ptlist[num][0], ptlist.ptlist[num][1]), (0, 255, 0), markerSize=round(h * 0.1), thickness=3)
                    cv2.circle(img2, (ptlist.ptlist[num][0], ptlist.ptlist[num][1]), round(h * 0.05), (255, 0, 0), thickness=3)
            cv2.imshow(wname, img2)
        else:
            print('All points have selected.  Press ESC-key.')
            
        if(ptlist.pos == ptlist.npoints):
            print(ptlist.ptlist)
            cv2.line(img, (ptlist.ptlist[0][0], ptlist.ptlist[0][1]),
                     (ptlist.ptlist[1][0], ptlist.ptlist[1][1]), (0, 255, 0), 3)
            cv2.line(img, (ptlist.ptlist[1][0], ptlist.ptlist[1][1]),
                     (ptlist.ptlist[2][0], ptlist.ptlist[2][1]), (0, 255, 0), 3)
            cv2.line(img, (ptlist.ptlist[2][0], ptlist.ptlist[2][1]),
                     (ptlist.ptlist[3][0], ptlist.ptlist[3][1]), (0, 255, 0), 3)
            cv2.line(img, (ptlist.ptlist[3][0], ptlist.ptlist[3][1]),
                     (ptlist.ptlist[0][0], ptlist.ptlist[0][1]), (0, 255, 0), 3)


if __name__ == '__main__':
    img = cv2.imread(input_file_path)
    wname = "MouseEvent"
    cv2.namedWindow(wname)
    npoints = 4
    ptlist = PointList(npoints)
    h, w = img.shape[0], img.shape[1]
    cv2.setMouseCallback(wname, onMouse, [wname, img, ptlist, h, w])
    cv2.imshow(wname, img)
    cv2.waitKey()


    # 比率調整
    w_ratio = 1

    # 変換前4点の座標　p1:左上　p2:右上 p3:右下 p4:左下
    # 時計回りで指定
    p1 = ptlist.ptlist[0]
    p2 = ptlist.ptlist[1]
    p3 = ptlist.ptlist[3]
    p4 = ptlist.ptlist[2]

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
