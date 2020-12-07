import os
import re

dir = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir}/input.txt", "r")
rules = input.read().splitlines()

### --- PARSING INPUT


def parse_rules(rules):
    top_down_dict = {}
    down_top_dict = {}

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
                down_top_dict[contained_color] = {container_color}
            else:
                down_top_dict[contained_color].add(container_color)

            top_down_dict[container_color][f"{des} {color}"] = int(count)

    return top_down_dict, down_top_dict


top_down_dict, down_top_dict = parse_rules(rules)


### --- PART I


def get_possible_containers(contained_color, possible_containers):
    if contained_color in down_top_dict:
        container_colors = down_top_dict[contained_color]
        possible_containers.update(container_colors)

        for container_color in container_colors:
            colors = get_possible_containers(container_color, possible_containers)
            possible_containers.update(colors)

    return possible_containers


possible_containers = get_possible_containers("shiny gold", set())
print(len(possible_containers))


### --- PART II


def count_contained_bags(init_container_color):
    total_contained_count = -1
    bags_to_count = [(1, init_container_color)]

    for count, container_color in bags_to_count:
        total_contained_count += count

        if container_color in top_down_dict:
            for color, contained_count in top_down_dict[container_color].items():
                bags_to_count.append((count * contained_count, color))

    return total_contained_count


print(count_contained_bags("shiny gold"))

