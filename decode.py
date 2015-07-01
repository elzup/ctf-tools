# -*- coding: utf-8 -*-
# import sys
import base64
# import uu
import re
import codecs

# if len(sys.argv) > 1:
#     v = sys.argv[1]
# else:
#     print("val?")
#     v = input()

v = 'c3:a3:c2:81:c2:8d:c3:a3:c2:82:c2:83:c3:a3:c2:81:c2:b7:c3:a3:c2:81:c2:a1:c3:a3:c2:82:c2:83:c3:a3:c2:83:c2:bc:c3:83:c2:a3:c3:82:c2:83:c3:82:c2:bb:c3:83:c2:a3:c3:82:c2:82:c3:82:c2:b6:c3:83:c2:a3:c3:82:c2:83:c3:82:c2:bb:e3:81:b5:e3:82:89:e3:81:a3:e3:81:90'

# vs = re.split('(..)', v)[1::2]
vs = v.split(':')

print(v + "(plain)")
print()
print("base64         : ", base64.b64encode(v.encode('ascii')))
print("base64dec      : ", base64.b64decode(v.encode('ascii')))
print("rot13          : ", codecs.encode(v, "rot-13"))
print("rot13dec       : ", codecs.decode(v, "rot-13"))
# # print("uu             : ", uu.encode(v))
# # print("uudec          : ", uu.decode(v))
# print()
# print("hex            : ", v.encode('hex'))
# print("hexdec         : ", v.decode('hex'))
# print("chr            : ", "".join(map(chr, map(int, vs))))
# print("inp16          : ", "".join(map(chr, map(lambda s: int(s, 16), vs))))
print("int16          : ", "".join(map(chr, map(lambda s: int(s, 16), vs))))
s = "".join(map(chr, map(lambda s: int(s, 16), vs)))

unienc = lambda s: ":".join([chr(int(c, 16)) for c in s.split(":")])
unidec = lambda s: ":".join("{:02x}".format(ord(c)) for c in s)
# print(unidec(a.encode('utf-8').encode('utf-8')))
print(unienc(v))

print("utf8           : ", v.encode('utf-8'))
print("utf8dec        : ", v.decode('utf-8'))
# print();
# print("url            : ", (url_escape_utf8($v)), "\n");
# print("urldec         : ", (url_unescape($v)), "\n");
