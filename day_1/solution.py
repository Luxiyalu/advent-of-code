import os

dir = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir}/input", "r")
arr = input.read().splitlines()


def calc_1():
    for i, a in enumerate(arr):
        for b in arr[i + 1 :]:
            if int(a) + int(b) == 2020:
                return int(a) * int(b)


def calc_2():
    for i, a in enumerate(arr):
        for j, b in enumerate(arr[i + 1 :]):
            for c in arr[j + 1 :]:
                if int(a) + int(b) + int(c) == 2020:
                    return int(a) * int(b) * int(c)

