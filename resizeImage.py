import os
import glob
from PIL import Image

# 이미지 크기 변환
files = glob.glob('Images/*.jpg')
i = 0

for f in files:
    img = Image.open(f)
    img_resize = img.resize((227, 227))
    title, ext = os.path.splitext(f)

    alpha = title[7]

    img_resize.save('Images_227/' + alpha + "/" + title[7:] + '.jpg')
