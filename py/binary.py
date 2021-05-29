# https://qiita.com/freedom865/items/f26b416ec2651c4b9c95
import sys
from PIL import Image

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

img = Image.open(input_file_path, 'r')
conv_image = img.convert("1")
conv_image.save(output_file_path)
