# advent of code day 12
import os

dir = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir}/input.txt", "r")
data = input.read().splitlines()

sin = {0: 0, 90: 1, 180: 0, 270: -1}
cos = {0: 1, 90: 0, 180: -1, 270: 0}

x = y = dir = 0
wx = 10
wy = 1
for op, val in [(x[:1], int(x[1:])) for x in data]:
    if op == "N":
        wy += val
    elif op == "S":
        wy -= val
    elif op == "E":
        wx += val
    elif op == "W":
        wx -= val
    elif op == "R":
        nwx = wx * cos[-val % 360] - wy * sin[-val % 360]
        nwy = wx * sin[-val % 360] + wy * cos[-val % 360]
        wx, wy = nwx, nwy
    elif op == "L":
        nwx = wx * cos[val % 360] - wy * sin[val % 360]
        nwy = wx * sin[val % 360] + wy * cos[val % 360]
        wx, wy = nwx, nwy
    else:
        x += val * wx
        y += val * wy
    print(wx, wy)

print(abs(x) + abs(y))

