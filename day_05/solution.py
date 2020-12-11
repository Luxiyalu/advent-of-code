import os
import re
from typing import List

dir = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir}/input.txt", "r")
passes = input.read().splitlines()


# PART 1
def get_highest_seat_id(passes: List[str]) -> int:
    FB_i = 0
    LR_i = 0
    row = 0
    column = 0

    while FB_i < 7 and len(passes) > 0:
        filtered_passes = list(filter(lambda p: p[FB_i] == "B", passes))

        if len(filtered_passes) > 0:
            passes = filtered_passes
            row += pow(2, 6 - FB_i)

        FB_i += 1

    while LR_i < 3 and len(passes) > 0:
        filtered_passes = list(filter(lambda p: p[7 + LR_i] == "R", passes))

        if len(filtered_passes) > 0:
            passes = filtered_passes
            column += pow(2, 2 - LR_i)

        LR_i += 1

    id = row * 8 + column

    assert len(passes) == 1
    return id


assert get_highest_seat_id(passes) == 987


### PART 2


def get_seat_id(pass_str: str) -> int:
    pass_str = re.sub(r"[FL]", "0", pass_str)
    pass_str = re.sub(r"[BR]", "1", pass_str)
    rows = int(pass_str[:-3], 2)
    columns = int(pass_str[-3:], 2)

    return rows * 8 + columns


assert get_seat_id("BFFFBBFRRR") == 567
assert get_seat_id("FFFBBBFRRR") == 119
assert get_seat_id("BBFFBBFRLL") == 820


def get_my_seat_id(passes):
    seat_ids = list(map(get_seat_id, passes))

    for seat_id in seat_ids:
        if seat_id + 2 in seat_ids and seat_id + 1 not in seat_ids:
            return seat_id + 1


assert get_my_seat_id(passes) == 603

