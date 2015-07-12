from unpyc3 import decompile


def foo(x, y, z=3, *args):
    global g
    for i, j in zip(x, y):
        if z == i + j or args[i] == j:
            g = i, j
            return

