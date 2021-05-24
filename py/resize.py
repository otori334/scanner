# https://qiita.com/haminiku/items/e53aa1d9bda77d2efe28
# アンチエイリアスが使える
# 多色画像の縮小が得意
# モノクロ画像に関しては大津の二値化などを用いた圧縮と比べて可読性も圧縮能力も劣る
import sys
from PIL import Image

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]
height = float(sys.argv[3])
#height=300

img = Image.open(input_file_path, 'r')

rows,cols = img.size
x = int(round(float(height / float(cols) * float(rows))))
y = height
#print("{}, {}".format(x, y))

resize_img = img

# アンチエイリアスの有無はデータサイズに影響しない
# アンチエイリアスありで縮小
resize_img.thumbnail((x, y), Image.ANTIALIAS)
# アンチエイリアスなしで縮小
#resize_img = resize_img.resize((x, y))

resize_img.save(output_file_path)
