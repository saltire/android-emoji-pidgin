import os

from PIL import Image


source = '../noto-emoji/png/128'
dest = './android-emoji-theme'

for imgfile in os.listdir(source):
    img = Image.open(os.path.join(source, imgfile))

    ratio = img.width / 25

    img = img.resize((25, int(img.height // ratio)), Image.ANTIALIAS)
    img.save(os.path.join(dest, imgfile))
