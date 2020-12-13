"""
NOTE:

- To split problems into smaller components
"""


import os
from typing import List, Tuple

dir = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir}/input.txt", "r")
instructions = input.read().splitlines()
instructions_test = ["F10", "N3", "F7", "R90", "F11"]


def coordinates(instructions: List[str], dis_E=0, dis_N=0) -> Tuple[int, int]:
    """
    Part 1: get coordinates of the ship at the end of list of instructions
    """
    dirs = ["E", "S", "W", "N"]
    dir_i = 0

    for instruction in instructions:
        ins = instruction[0]
        num = int(instruction[1:])

        if ins == "F":
            ins = dirs[dir_i]

        if ins == "E":
            dis_E += num
        elif ins == "W":
            dis_E -= num
        elif ins == "N":
            dis_N += num
        elif ins == "S":
            dis_N -= num
        elif ins == "R":
            times = int(num / 90)
            dir_i = (dir_i + times) % 4
        elif ins == "L":
            times = int(num / 90)
            dir_i = (dir_i - times) % 4

    return dis_E, dis_N


print(coordinates(instructions))


def turn_coordinates(x, y, times):
    """
    Helper function to turn coordinates in Part II

    TODO: is there a better way to do this?
    """
    assert 0 <= times <= 3

    if times == 0:
        return x, y
    if times == 1:
        if (x >= 0 and y >= 0) or (x <= 0 and y <= 0):
            return y, 0 - x
        if (x >= 0 and y <= 0) or (x <= 0 and y >= 0):
            return y, 0 - x
    if times == 2:
        return 0 - x, 0 - y
    if times == 3:
        return turn_coordinates(0 - x, 0 - y, 1)


assert turn_coordinates(3, 1, 1) == (1, -3)
assert turn_coordinates(1, -3, 1) == (-3, -1)
assert turn_coordinates(-3, -1, 1) == (-1, 3)
assert turn_coordinates(-1, 3, 1) == (3, 1)
assert turn_coordinates(1, 3, 2) == (-1, -3)
assert turn_coordinates(3, 1, 3) == (-1, 3)
assert turn_coordinates(13, 0, 3) == (0, 13)


def manhattan_distance(instructions: List[str]) -> int:
    """
    PART II: get manhattan_distance of the ship from its initial position
    """
    way_x, way_y = 10, 1
    ship_x, ship_y = 0, 0

    for instruction in instructions:
        ins = instruction[0]
        num = int(instruction[1:])

        if ins == "F":
            ship_x += way_x * num
            ship_y += way_y * num

        elif ins in ["E", "S", "W", "N"]:
            way_x, way_y = coordinates([instruction], way_x, way_y)

        elif ins in ["R", "L"]:
            num = 0 - num if ins == "L" else num
            times = int((num / 90) % 4)
            way_x, way_y = turn_coordinates(way_x, way_y, times)

    return abs(ship_x) + abs(ship_y)


print(manhattan_distance(instructions))
