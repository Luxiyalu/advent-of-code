import os
import re
from typing import Callable, List

dir = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir}/input.txt", "r")
passports = input.read().split("\n\n")

REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


class Validator:
    def __init__(self, fields: str) -> None:
        self.fields = fields
        self.values = {}

        for field_whole in fields.split(" "):
            (field, value) = field_whole.split(":")
            self.values[field] = value

    def field_is_valid(self, field: str) -> bool:
        if field in self.values:
            value = self.values[field]
            validator = getattr(self, field)

            return validator(value)

    def fields_are_valid(self) -> bool:
        return all(self.field_is_valid(field) for field in REQUIRED_FIELDS)

    def byr(self, val: str) -> bool:
        year = int(val)

        return len(val) == 4 and 1920 <= year <= 2002

    def iyr(self, val: str) -> bool:
        year = int(val)

        return len(val) == 4 and 2010 <= year <= 2020

    def eyr(self, val: str) -> bool:
        year = int(val)

        return len(val) == 4 and 2020 <= year <= 2030

    def hgt(self, val: str) -> bool:
        if val.endswith("cm"):
            return 150 <= int(val[:-2]) <= 193

        if val.endswith("in"):
            return 59 <= int(val[:-2]) <= 76

    def hcl(self, val: str) -> bool:
        hex = re.compile(r"^#[a-fA-F0-9]{6}$")

        return bool(hex.match(val))

    def ecl(self, val: str) -> bool:
        return val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def pid(self, val: str) -> bool:
        return len(val) == 9


def fields_are_valid_part_1(fields: str) -> bool:
    return all((field in fields for field in REQUIRED_FIELDS))


def fields_are_valid_part_2(fields: str) -> bool:
    return Validator(fields).fields_are_valid()


def count_valid(check_is_valid: Callable) -> int:
    count = 0

    for passport in passports:
        if check_is_valid(passport.replace("\n", " ").strip()):
            count += 1

    return count


print(count_valid(fields_are_valid_part_1))
print(count_valid(fields_are_valid_part_2))
