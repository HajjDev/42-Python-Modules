#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/29 14:14:32 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 16:24:02 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# --- Different Error Types ---

class GardenError(Exception):
    """
    This class creates a new custom error, GardenError related to all errors
    regarding a garden.
    """
    def __init__(self, message: str) -> None:
        """
        This function initializes the GardenError class with a custom
        message.

        Args:
            message (str): The message to be displayed
        """
        super().__init__(message)


class PlantError(GardenError):
    """
    This class creates a new custom error, PlantError of type GardenError
    related to all errors regarding a plant in a garden.
    """
    def __init__(self, message: str) -> None:
        """
        This function initializes the PlantError class with a custom
        message using the __init__ function of it's super class.

        Args:
            message (str): The message to be displayed
        """
        super().__init__(message)


class WaterError(GardenError):
    """
    This class creates a new custom error, WaterError of type GardenError
    related to all errors regarding water in a garden.
    """
    def __init__(self, message: str) -> None:
        """
        This function initializes the PlantError class with a custom
        message using the __init__ function of it's super class.

        Args:
            message (str): The message to be displayed
        """
        super().__init__(message)


# --- Different Functions and Classes to demonstrate error raising
# and catching ---
class Plant:
    """
    This class represents a Plant object. A plant object is represented
    by a name and a water level.
    """
    def __init__(self, name: str, water_level: int) -> None:
        """
        This function initializes the plant object with the following
        attributes.

        Args:
            name (str): The name of the plant
            water_level (int): The water level of the plant
        """
        self.name = name
        self.water_level = water_level


class Tank:
    """
    This class represents a Tank object. A tank object is represented
    by a water level.
    """
    def __init__(self, water: int) -> None:
        """
        This function initializes the tank object with the following
        attributes.

        Args:
            water (int): The water level of the tank
        """
        self.water = water


def plant_check(plant: Plant) -> None:
    """
    This function is used to check if a plant has a certain
    water level.

    Args:
        plant (Plant): The plant to be checked

    Raises:
        PlantError: If the water level is lower than 40
    """
    if plant.water_level < 40:
        raise PlantError(f"The {plant.name} plant is wilting!")
    else:
        print(f"The {plant.name} plant is in shape.")


def tank_check(tank: Tank) -> None:
    """
    This function is used to check if a tank has a certain
    water level.

    Args:
        tank (Tank): The tank to be checked

    Raises:
        WaterError: If the water level of the tank is lower than
        300L
    """
    if tank.water < 300:
        raise WaterError("Not enough water in the tank!")


def plant_error_demo() -> None:
    """
    This function demonstrates the proper function of the PlantError.
    """
    print("Testing PlantError...")
    plant = Plant("tomato", 20)
    try:
        plant_check(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")


def tank_error_demo() -> None:
    """
    This function demonstrates the proper function of the WaterError.
    """
    print("Testing WaterError...")
    tank = Tank(200)
    try:
        tank_check(tank)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")


def garden_error_demo() -> None:
    """
    This function demonstrates the proper function of the GardenError.
    """
    print("Testing GardenError...")
    plant = Plant("tomato", 20)
    tank = Tank(200)
    try:
        plant_check(plant)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        tank_check(tank)
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")


# --- Tests and Main program ---
if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    plant_error_demo()
    tank_error_demo()
    garden_error_demo()

    print("All custom error types work correctly!")
