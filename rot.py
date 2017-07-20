# -*- coding: utf-8 -*-
import sys

def rot_n(v, n):
    lib = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    t = ''
    for j, c in enumerate(list(v.strip())):
        if c not in lib:
            t += c
            continue
        k = lib.find(c)
        t += lib[(k + n + 52) % 52]
    print("rot{0:2d}".format(n), t)


def rot13(v):
    rot_n(v, 13)


def rot_all(v):
    for i in range(52):
        rot_n(v, i)


def rot_chr(v, n):
    t = ''
    for j, c in enumerate(list(v)):
        t += chr(ord(c) + n)
    return t


def encode_greek(v):
    t = ''
    lib = {"Α": "A", "Β": "V", "Γ": "G", "Δ": "D", "Ε": "E",
           "Ζ": "Z", "Η": "I", "Θ": "TH", "Ι": "I", "Κ": "K",
           "Λ": "L", "Μ": "M", "Ν": "N", "Ξ": "KS", "Ο": "O",
           "Π": "P", "Ρ": "R", "Σ": "S", "Τ": "T", "Υ": "I",
           "Φ": "F", "Χ": "CH", "Ψ": "PS", "Ω": "O"}
    for j, c in enumerate(list(v)):
        print(c)
        if c in lib:
            print(c)
            t += lib[c]
            continue
        t += c
    return t

# v = 'print get_pass'
# rot_all(v)

# v = 'rKrUl+/clKHb4u/sm6sgnaPfnO/XkO=ewqPU45bRjp4gwa7NntoM467Onu/enqPRlakgj6Egjp0e1gAA'
# print(rot_chr(v, -4))
# nGnQh'+_hGD^0q+oi2ocj]LbjK+TgK9asmLQ01^Nfl0cs]3JjpkI023Kjq+ajmLNh]gcf2Acfl,a-c==

# v = 'ΥΔΗΖΙΝΔJΙ-ΧJΙΟΜJGGΔΙΒ ΑJΜΟ "ΥJΓ" ΓΥΝ ΙJΡ WΖΖΙ ΥΖΗJGΔΝΓΖΥ, ΥΙΥ ΟΔΗΖ ΝΟΥΜΟΖΥ ΑGJΡΔΙΒ ΜΖQΖΜΝΖGΤ. "QΥΠΝ" ΗΥΙΥΒΖΥ ΟJ ΖΝΧΥΚΖ ΑΜJΗ ΟΓΖ ΥΔΝΟJΜΟΖΥ ΝΚΥΧΖ. WΠΟ ΟΓΖ ΜΖΥG QJΤΥΒΖ JΑ "ΥΜFΥΙJΔΥ" ΔΙ ΟΓΖ ΒΥGΥΣΤ ΓΥΝ JΙGΤ ΝΟΥΜΟΖΥ......'
v = 'ydizindji-xjiomjggdib ajmo "yjg" gyn ijp wzzi yzhjgdngzy, yiy odhz noymozy agjpdib mzqzmnzgt. "qypn" hyiybzy qj znxykz amjh ogz ydnojmozy nkyxz. wpo ogz mzyg qjtybz ja "ymfyijdy" di ogzb ygyst gyn jigt noymozy......'
if len(sys.argv) >= 2:
    v = sys.argv[1]
rot_all(v)
# print(encode_greek(v))

