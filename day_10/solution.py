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


### --- PART II: top-down


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


def calc_v1(l):
    v = count_arrangements([0, *l], {})

    return v


assert calc_v1([1]) == 1
assert calc_v1([1, 2]) == 2
assert calc_v1([1, 2, 3]) == 4
assert calc_v1([3, 4, 5]) == 2

print(calc_v1(adaptors))


### -- PART II: bottom-up (tree) + recursive


def count_arrangements_v2(adaptors):
    adaptors = [0, *adaptors]

    def f(i):
        if i + 1 == len(adaptors):
            return 1

        count = 0

        if adaptors[i + 1] - adaptors[i] <= 3:
            count += f(i + 1)
        if i + 2 < len(adaptors) and adaptors[i + 2] - adaptors[i] <= 3:
            count += f(i + 2)
        if i + 3 < len(adaptors) and adaptors[i + 3] - adaptors[i] <= 3:
            count += f(i + 3)

        return count

    return f(0)

