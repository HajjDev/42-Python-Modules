#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_errors.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/29 15:08:15 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 15:29:09 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """
    This function checks if a plant is healthy. A healthy plant has a
    valid name (not empty), a water level between 1 and 10 and sunlight
    hours between 2 and 12.

    Args:
        plant_name (str): The name of plant
        water_level (int): The water level of the plant
        sunlight_hours (int): The sunlight hours of the plant
    """
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    elif water_level < 1 or water_level > 10:
        if water_level < 0:
            raise ValueError("Error: Water level cannot be negative!")
        elif water_level < 1:
            raise ValueError(f"Error: Water level {water_level} \
is too low (min 1)")
        else:
            raise ValueError(f"Error: Water level {water_level} is too high \
(max 10)")
    elif sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours < 0:
            raise ValueError("Error: Sunlight hours cannot be negative!")
        elif sunlight_hours < 1:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} \
is too low (min 2)")
        else:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too \
high (max 12)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """
    This function tests and demonstrates that all of the different errors
    are handled correctly.
    """
    print("Testing good values...")
    check_plant_health("tomato", 5, 5)
    print("")

    try:
        print("Testing empty plant name...")
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(e)
    print("")

    try:
        print("Testing bad water level...")
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(e)
    print("")

    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(e)
    print("")


# --- Tests and Main program ---
if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("All error raising tests completed!")
