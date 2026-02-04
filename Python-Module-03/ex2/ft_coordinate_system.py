#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/29 17:12:28 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/30 19:08:25 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# --- Package imports ---
import math


def parse_coordinates(coordinates: str) -> tuple[int, int, int] | None:
    """
    This function parses the coordinates from a string into a tuple.

    Args:
        coordinates (str): The coordinates to parse in the form of a string.

    Returns:
        tuple[int, int, int] | None: A tuple of the coordinates if
        all of the coordinates are valid (integers), None otherwise.
    """
    parsed_nums = coordinates.split(",")
    try:
        x = int(parsed_nums[0])
        y = int(parsed_nums[1])
        z = int(parsed_nums[2])
        return (x, y, z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: ValueError, Args: ("{e}",)')
        return None


def euclidian_distance(p1: tuple[int, int, int],
                       p2: tuple[int, int, int] | None) -> float:
    """
    This function calculates the euclidian distance between
    2 points using the formula:
    math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2

    Args:
        p1 (tuple[int, int, int]): The first point
        p2 (tuple[int, int, int] | None): The second point

    Returns:
        float: The euclidian distance of the 2 points
    """
    if (p2 is None):
        return 0
    squared_dist = (p2[0] - p1[0]) ** 2 + \
        (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2
    return math.sqrt(squared_dist)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    null_vector = (0, 0, 0)
    p1 = (10, 20, 5)
    valid_coordinates_to_parse = "3,4,0"
    invalid_coordinates_to_parse = "abc,def,ghi"

    print(f"Position created: {p1}")
    print(f"Distance between {null_vector} and {p1}: \
{euclidian_distance(null_vector, p1):.2f}\n")

    print(f'Parsing coordinates: "{valid_coordinates_to_parse}"')
    parsed_coordinates = parse_coordinates(valid_coordinates_to_parse)
    print(f"Parsed position: {parsed_coordinates}")
    print(f"Distance between {null_vector} and {parsed_coordinates}: \
{euclidian_distance(null_vector, parsed_coordinates)}\n")

    print(f'Parsing invalid coordinates: "{invalid_coordinates_to_parse}"')
    parse_coordinates(invalid_coordinates_to_parse)

    print("\nUnpacking demonstration:")
    print("Player at x=3, y=4, z=0")
    unpacked_coordinates = parse_coordinates("3,4,0")
    if unpacked_coordinates is not None:
        x, y, z = unpacked_coordinates
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
