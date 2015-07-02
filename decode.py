# -*- coding: utf-8 -*-
# import sys
import base64
# import uu
import re
import codecs
import chardet


def zip2(arr):
    return [arr[i] + arr[i + 1] for i in range(0, len(arr), 2)]


def char_code_all(text):
    encodings = ['iso-2022-jp', 'euc-jp', 'euc-jisx0213', 'euc-jis-2004', 'iso-2022-jp',
                 'iso-2022-jp-1', 'iso-2022-jp-2', 'iso-2022-jp-3', 'iso-2022-jp-ext',
                 'iso-2022-jp-2004', 'utf-7', 'utf-8', 'utf-16', 'utf-16-be', 'utf-16-le',
                 'cp932', 'shift-jis', 'shift-jisx0213', 'shift-jis-2004']
    for enc in encodings:
        try:
            k = text.decode(enc)
        except (UnicodeDecodeError, UnicodeEncodeError):
            print("Inv: " + enc)
            continue
        print("Match: " + enc)
        print(k)

# if len(sys.argv) > 1:
#     v = sys.argv[1]
# else:
#     print("val?")
#     v = input()
str = 'document.domain'
print("".join(['\\x{0:X}'.format(ord(c)) for c in list(str)]))

v = 'c3:a3:c2:81:c2:8d:c3:a3:c2:82:c2:83:c3:a3:c2:81:c2:b7:c3:a3:c2:81:c2:a1:c3:a3:c2:82:c2:83:c3:a3:c2:83:c2:bc:c3:83:c2:a3:c3:82:c2:83:c3:82:c2:bb:c3:83:c2:a3:c3:82:c2:82:c3:82:c2:b6:c3:83:c2:a3:c3:82:c2:83:c3:82:c2:bb:e3:81:b5:e3:82:89:e3:81:a3:e3:81:90'

# vs = re.split('(..)', v)[1::2]
vs = v.split(':')
v = "".join(vs)

print(vs)
a = "".join(map(lambda s: s.decode('hex'), vs))
print(a)
print(chardet.detect(a))
char_code_all(a)
# print("".join(map(chr, map(lambda s: int(s, 10), vs))))

print(v + "(plain)")
print()
print("base64         : ", base64.b64encode(v.encode('ascii')))
print("base64dec      : ", base64.b64decode(v.encode('ascii')))
print("rot13          : ", codecs.encode(v, "rot-13"))
print("rot13dec       : ", codecs.decode(v, "rot-13"))
# # print("uu             : ", uu.encode(v))
# # print("uudec          : ", uu.decode(v))
# print()
print("hex            : ", v.encode('hex'))
print("hexdec         : ", v.decode('hex'))
# print("chr            : ", "".join(map(chr, map(int, vs))))
# print("inp16          : ", "".join(map(chr, map(lambda s: int(s, 16), vs))))
print("int16          : ", "".join(map(chr, map(lambda s: int(s, 16), vs))))
# print(unienc(v))

print("utf8           : ", v.encode('utf-8'))
print("utf8dec        : ", v.decode('utf-8'))
# print();
# print("url            : ", (url_escape_utf8($v)), "\n");
# print("urldec         : ", (url_unescape($v)), "\n");

s = "".join(map(chr, map(lambda s: int(s, 16), vs)))

unienc = lambda s: ":".join([chr(int(c, 16)) for c in s.split(":")])
unidec = lambda s: ":".join("{:02x}".format(ord(c)) for c in s)
print(vs)

li = []
for i in range(len(vs) / 2):
    c = vs[i] + vs[i + 1]
    li.append('\\x' + c)
print(("".join(li)).encode('ascii'))
print(("".join(li)).encode('utf8'))

v2 = "".join(vs)
v2b = base64.b64decode(v2.encode('ascii'))
print(v2b)
print(v2b.encode('hex'))
print(base64.b64decode((v2b.encode('hex')).encode('ascii')))
# print(v2b.decode('hex'))
v2 = list(v2b)
print(v2)
v2 = zip2(v2)
print(v2)
# print(unidec(a.encode('utf-8').encode('utf-8')))


