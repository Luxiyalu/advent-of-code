import os
import re
from typing import List, Tuple

dir = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir}/input.txt", "r")
rules = input.read().splitlines()

### --- PARSING INPUT


def parse_rules(rules: List[str]) -> Tuple[dict, dict]:
    top_down_dict = {}  # container -> contained map
    down_top_dict = {}  # contained -> container map

    for rule in rules:
        if "no other bags" in rule:
            continue

        container_color, contained_str = rule.split(" bags contain ")
        contained_colors = re.sub(r"\sbag(s)*\.*", "", contained_str).split(", ")

        top_down_dict[container_color] = {}
        for contained_color_str in contained_colors:
            count, des, color = contained_color_str.split(" ")
            contained_color = f"{des} {color}"

            if contained_color not in down_top_dict:
                down_top_dict[contained_color] = set()

            down_top_dict[contained_color].add(container_color)
            top_down_dict[container_color][f"{des} {color}"] = int(count)

    return top_down_dict, down_top_dict


top_down_dict, down_top_dict = parse_rules(rules)


### --- PART I


def get_possible_containers(contained_color: str) -> int:
    containers_to_count = [contained_color]

    for color in containers_to_count:
        if color not in down_top_dict:
            continue

        for container_color in down_top_dict[color]:
            if container_color not in containers_to_count:
                containers_to_count.append(container_color)

    return len(containers_to_count) - 1


print(get_possible_containers("shiny gold"))


### --- PART II


def count_contained_bags(init_container_color: str) -> int:
    total_bags_count = -1
    bags_to_count = [(init_container_color, 1)]

    for container_color, bag_count in bags_to_count:
        total_bags_count += bag_count

        if container_color in top_down_dict:
            for color, count in top_down_dict[container_color].items():
                bags_to_count.append((color, bag_count * count))

    return total_bags_count


print(count_contained_bags("shiny gold"))

