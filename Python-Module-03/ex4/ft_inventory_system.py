#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/30 19:21:06 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/04 12:53:30 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def parse_input() -> dict[str, int] | None:
    parsed_input: dict[str, int] = {}
    parsing_key = True
    current_key: str = ""
    current_value = ""
    try:
        for item in sys.argv[1:]:
            for char in item:
                if char == ":":
                    parsing_key = False
                    continue
                if parsing_key and char != " ":
                    current_key += char
                elif char != " ":
                    current_value += char
                else:
                    parsed_input[current_key] = int(current_value)
                    current_key = ""
                    current_value = ""
                    parsing_key = True
            if current_value != "" and current_key != "":
                parsed_input[current_key] = int(current_value)
                current_key = ""
                current_value = ""
                parsing_key = True
        if parsed_input == {}:
            return None
        return parsed_input
    except Exception:
        print("Invalid Input, a valid input format looks like \
({sword: 1 shield: 2 armor: 3 helmet: 1})")
        return None


if __name__ == "__main__":
    items = parse_input()
    if items is not None:
        print("=== Inventory System Analysis ===")
        total_values = 0
        for val in items.values():
            total_values += val
        print(f"Total items in inventory: {total_values}")
        print(f"Unique item types: {len(items)}\n")

        print("=== Current Inventory ===")
        for item, val in items.items():
            print(f"{item}: {val} units ({((val / total_values) * 100):.1f}%)")
        print("")

        most: tuple[str, float] = ("", float("-inf"))
        least: tuple[str, float] = ("", float("inf"))
        for item, val in items.items():
            if val > most[1]:
                most = (item, val)
            elif val < least[1]:
                least = (item, val)
        if least[1] == float("inf"):
            least = ("None", 0)
        if most[1] == float("-inf"):
            most = ("None", 0)

        print("=== Inventory Statistics ===")
        print(f"Most abundant: {most[0]} ({most[1]} units)")
        print(f"Least abundant: {least[0]} \
({least[1]} units)\n")

        moderate: dict[str, int] = {}
        scarce: dict[str, int] = {}
        for item, val in items.items():
            if val < 5:
                scarce[item] = val
            else:
                moderate[item] = val
        print("=== Item Categories ===")
        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}\n")

        print("=== Management Suggestions ===")
        restocks: list[str] = [n for n in items.keys() if items[n] == least[1]]
        print(f"Restock needed: {restocks}")
        print("")

        print("=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {items.keys()}")
        print(f"Dictionary values: {items.values()}")
        print(f"Sample lookup - 'sword' in inventory: \
{items.get('sword') is not None}")
