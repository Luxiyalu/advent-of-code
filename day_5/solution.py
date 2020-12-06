import os
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
    assert get_seat_id(passes[0]) == id
    return id


print(get_highest_seat_id(passes))


### PART 2
def get_row(rows_str: str) -> int:
    row = 0
    for i in range(7):
        if rows_str[i] == "B":
            row += pow(2, 6 - i)

    return row


def get_column(columns_str: str) -> int:
    column = 0
    for i in range(3):
        if columns_str[i] == "R":
            column += pow(2, 2 - i)

    return column


def get_seat_id(pass_str: str) -> int:
    rows_str = pass_str[:-3]
    column_str = pass_str[-3:]

    return get_row(rows_str) * 8 + get_column(column_str)


assert (get_row("BFFFBBF")) == 70
assert get_seat_id("BFFFBBFRRR") == 567
assert get_seat_id("FFFBBBFRRR") == 119
assert get_seat_id("BBFFBBFRLL") == 820


def get_my_seat_id(passes):
    seat_ids = list(map(get_seat_id, passes))

    for seat_id in seat_ids:
        if seat_id + 2 in seat_ids and seat_id + 1 not in seat_ids:
            return seat_id + 1


print(get_my_seat_id(passes))

