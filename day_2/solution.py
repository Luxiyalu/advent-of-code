import os

dir = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir}/input.txt", "r")
lines = input.read().splitlines()


def is_password_valid_part_1(line: str) -> bool:
    (range_str, char_str, password) = line.split()
    lower_bount, upper_bound = [int(r) for r in range_str.split("-")]
    char = char_str.replace(":", "")
    occurance = password.count(char)

    return lower_bount <= occurance <= upper_bound


def is_password_valid_part_2(line: str) -> bool:
    (positions_str, char_str, password) = line.split()
    index_a, index_b = [int(p) - 1 for p in positions_str.split("-")]
    char = char_str.replace(":", "")

    return (password[index_a] == char) ^ (password[index_b] == char)


sum_1 = sum(is_password_valid_part_1(l) for l in lines)
sum_2 = sum(is_password_valid_part_2(l) for l in lines)

print(sum_1, sum_2)
