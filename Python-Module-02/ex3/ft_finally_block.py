#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/29 14:42:12 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 16:25:33 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class InvalidPlant(Exception):
    """
    This class represents the InvalidPlant exception. This class is
    represented by a custom message.
    """
    def __init__(self, message: str) -> None:
        """
        This function initializes the exception with the following
        attributes.

        Args:
            message (str): The message to be displayed
        """
        super().__init__(message)


def water_plants(plant_list: list[object]) -> None:
    """
    This function opens a watering system and waters
    each valid plant in the list.

    Args:
        plant_list (list[object]): The list of plants
        to be watered

    Raises:
        InvalidPlant: If the plant is invalid, a plant is
        invalid if it's name is not a string
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant.__class__.__name__ != "str":
                raise InvalidPlant(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except InvalidPlant as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    This function tests the system and demonstrates the efficiency of
    the finally block.
    """
    # --- Test without errors ---
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("\nTesting with error...")
    water_plants(["tomato", None])


# --- Tests and Main program
if __name__ == "__main__":
    print("=== Garden Watering Systems ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
