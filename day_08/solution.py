import os
from typing import List, Tuple

dir = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir}/input.txt", "r")
instructions = [ins.split(" ") for ins in input.read().splitlines()]


def follow_instructions_part_1(instructions: List[str]):
    visited = {}
    i = 0
    accumulator = 0

    while i not in visited:
        command, num = instructions[i]
        num = int(num)

        visited[i] = True

        if command == "acc":
            accumulator += num
            i += 1
        if command == "jmp":
            i += num
        if command == "nop":
            i += 1

    return accumulator


print(follow_instructions_part_1(instructions))


def follow_instructions_part_2(instructions: List[str], flip_index) -> Tuple[bool, int]:
    visited = {}
    i = 0
    accumulator = 0

    while i not in visited:
        command, num = instructions[i]
        num = int(num)

        if i == flip_index:
            if command == "jmp":
                command = "nop"
            elif command == "nop":
                command = "jmp"

        visited[i] = True

        if command == "acc":
            accumulator += num
            i += 1
        elif command == "jmp":
            i += num
        elif command == "nop":
            i += 1

        if i == len(instructions):  # end is reached
            return True, accumulator

    return False, accumulator


def walkthrough(instructions: List[str]):
    for i in range(len(instructions)):
        reaches_end, accumucator = follow_instructions_part_2(instructions, i)

        if reaches_end:
            return accumucator


accumucator = walkthrough(instructions)

print(accumucator)
