import math
import os

dir = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir}/input.txt", "r")
rows = input.read().splitlines()


def count_trees(pace_x: int, pace_y: int) -> int:
    count = 0
    x_index = 0
    y_index = 0
    width = len(rows[0])

    while y_index < len(rows):
        char = rows[y_index][x_index]
        if char == "#":
            count += 1

        y_index += pace_y
        x_index = (x_index + pace_x) % width

    return count


res = (
    count_trees(1, 1),
    count_trees(3, 1),
    count_trees(5, 1),
    count_trees(7, 1),
    count_trees(1, 2),
)

print(math.prod(res))
