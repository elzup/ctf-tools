from PIL import Image
import sys
from qr import *

def scan(img, top, left, msize, version):
    w = h = version * 4 + 17
    qr = []
    for y in range(h):
        line = []
        for x in range(w):
            c = img.getpixel((top + msize * x, left + msize * y))
            if c == (0, 0, 0):
                x = 1
            elif c == (255, 255, 255):
                x = 0
            else:
                x = None
            line.append(x)
        qr.append(line)
    return qr

version = 3
qrcode_size = version * 4 + 17
module_size = 3

img = Image.open("qrgarden.png")
img = img.convert('RGB')
for y in range(0, 100):
    for x in range(100):
        qrtxt = scan(img, 29*module_size*x, 29*module_size*y, module_size, version)
        print(read_qr(qrtxt))
