# -*- coding: utf-8 -*-
import hashlib
import itertools

lib = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん', 'が', 'ぎ', 'ぐ', 'げ', 'ご', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 'だ', 'ぢ', 'づ', 'で', 'ど', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ']
# lib = ['ひ', 'ら', 'が', 'な']
lib = "tes"

filename = 'tes:'
# saltapeter
h = hashlib.md5('salt' + filename + 'peter').hexdigest()
print(h)
print(filename + ".png?accesscode=" + h)
exit()
# 9bac8e16f9c2eda4966a686cd389d293

# # 多重ハッシュ
# h = hashlib.md5(lib).hexdigest()
# for i in range(10000):
#     h = hashlib.md5(h).hexdigest()
#     print(h)
# exit()

# # strpos パターン
# h = hashlib.md5(lib).hexdigest()
# for s in range(7):
#     for e in range(7):
#         for d in [1, -1, 2, 3]:
#             for i in range(1, 3):
#                 tar = lib[s:e:d]
#                 if tar == "":
#                     continue
#                 h = hashlib.md5(tar).hexdigest()
#                 for i in range(i - 1):
#                     h = hashlib.md5(h).hexdigest()
#                 print(str(s) + ":" + str(e) + "[" + tar + "] " + h)
# exit()

ans = 'ce8c7fe2dec0baeaba8cb2590adbc478'
# # 順列
n = 3
for i in list(itertools.product(range(len(lib)), repeat=n)):
    s = ""
    for j in range(n):
        s += lib[i[j]]

    # h = hashlib.md5(s)
    h = hashlib.md5(s).hexdigest()
    print(h + ": " + s)
    if ans == h:
        print(h)
        break
