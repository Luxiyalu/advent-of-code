import os
from typing import List

dir = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir}/input.txt", "r")
groups = input.read().split("\n\n")

# --- PART 1


def count_group_answers_part_1(group_input):
    return len(set.union(*(set(p) for p in group_input.strip().split("\n"))))


assert count_group_answers_part_1("abc") == 3
assert count_group_answers_part_1("a\nb\nc") == 3
assert count_group_answers_part_1("ab\nac") == 3

print(sum(map(count_group_answers_part_1, groups)))


# --- PART 2


def count_group_answers_part_2(group_input):
    return len(set.intersection(*(set(p) for p in group_input.strip().split("\n"))))


assert count_group_answers_part_2("abc") == 3
assert count_group_answers_part_2("a\nb\nc") == 0
assert count_group_answers_part_2("ab\nac") == 1
assert count_group_answers_part_2("a\na\na\na") == 1
assert count_group_answers_part_2("b") == 1
assert count_group_answers_part_2("b\n") == 1

print(sum(map(count_group_answers_part_2, groups)))
