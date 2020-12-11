import os
from typing import List, Tuple

dir = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir}/input.txt", "r")
adaptors = [int(a) for a in input.read().splitlines()]
adaptors.sort()


def count_jolts(adaptors):
    jolt_curr = 0
    jolt_prev = 0
    jolt_1 = 0
    jolt_3 = 1

    for jolt in adaptors:
        jolt_curr = jolt
        delta = jolt_curr - jolt_prev

        if delta == 1:
            jolt_1 += 1
        if delta == 3:
            jolt_3 += 1

        jolt_prev = jolt_curr

    return (jolt_1, jolt_3)


def count_arrangements(adaptors, map):
    key = frozenset(adaptors[-3:])

    if key not in map:
        if len(adaptors) == 0:
            map[key] = 0
        elif len(adaptors) == 1:
            map[key] = 1
        elif len(adaptors) == 2:
            a, b = adaptors
            if a == 0:  # at the start of list
                map[key] = 1
            elif b <= 3:  # can skip a
                map[key] = 2
            else:  # have to include a
                map[key] = 1

        else:
            *rest, x, y, z = adaptors
            can_skip_y = z - x <= 3

            if can_skip_y:
                skip_y = count_arrangements([*rest, x, z], map)
                not_skip_y = count_arrangements([*rest, x, y], map)
                map[key] = skip_y + not_skip_y
            else:
                map[key] = count_arrangements([*rest, x, y], map)

    return map[key]


def calc(l):
    v = count_arrangements([0, *l], {})

    return v


assert calc([1]) == 1
assert calc([1, 2]) == 2
assert calc([1, 2, 3]) == 4
assert calc([3, 4, 5]) == 2

print(calc(adaptors))
