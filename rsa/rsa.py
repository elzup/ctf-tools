# -*- coding: utf-8 -*-
p = 193
q = 11
e = 77

n = p * q

def gcd(a, b):
    if b == 0:
        u = 1
        v = 0
    else:
        q = a / b
        r = a % b
        (u0, v0) = gcd(b, r)
        u = v0
        v = u0 - q * v0
    return (u, v)

def lcm(a, b):
    return a * b / gcd(a, b)

l = lcm(p - 1, q - 1)
d = gcd(e, l)[0]
if d < 0:
    d += l

pow(x, d, n)
