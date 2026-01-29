#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/29 15:30:50 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 16:29:11 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

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


class Plant:
    """
    This class represents a Plant. A plant is characterized by many attributes
    including a name, water level and sunlight hours.
    """
    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        """
        This method initializes the plant with the following attributes.

        Args:
            name (_type_): The name of the plant
            water_hours (_type_): The water hours of the plant
            sunlight_hours (_type_): The sunlight hours of the plant
        """
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


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


class GardenManager:
    """
    This class represents a garden. A garden can be characterized by it's
    plants.
    It can also perform various operations on it's own plants.
    """
    def __init__(self, plants: list[Plant], tank: Tank) -> None:
        """
        This method initializes the garden with the following attributes.

        Args:
            plants (list[Plant]): The list of plants in the garden
        """
        self.plants = plants
        self.water_tank = tank

    def add_plant(self, plant: Plant) -> None:
        """
        This method adds a plant to the garden only if the plant is valid.
        A plant is valid if it's name is not empty.

        Args:
            plant (Plant): The plant to be added
        """
        try:
            if plant.name != "":
                self.plants.append(plant)
                print(f"Added {plant.name} successfully")
            else:
                raise PlantError("Plant name cannot be empty!")
        except GardenError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        """
        This function opens a watering system and waters
        each valid plant in the list.

        Raises:
            InvalidPlant: If the plant is invalid, a plant is
            invalid if it's name is not a string
        """
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant.__class__.__name__ != "Plant":
                    raise PlantError(f"Cannot water {plant} - invalid plant!")
                print(f"Watering {plant.name} - success")
        except GardenError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plants_health(self) -> None:
        """
        This function checks if a plant is healthy. A healthy plant has a
        valid name (not empty), a water level between 1 and 10 and sunlight
        hours between 2 and 12.

        Args:
            plant_name (str): The name of plant
            water_level (int): The water level of the plant
            sunlight_hours (int): The sunlight hours of the plant
        """
        for plant in self.plants:
            try:
                if plant.water_level < 1 or plant.water_level > 10:
                    if plant.water_level < 0:
                        raise ValueError(f"Error checking {plant.name}: \
Water level cannot be negative!")
                    elif plant.water_level < 1:
                        raise ValueError(f"Error checking {plant.name}: \
Water level {plant.water_level} is too low (min 1)")
                    else:
                        raise ValueError(f"Error checking {plant.name}: \
Water level {plant.water_level} is too high (max 10)")
                elif plant.sunlight_hours < 2 or plant.sunlight_hours > 12:
                    if plant.sunlight_hours < 0:
                        raise ValueError("Error checking {plant.name}: \
Sunlight hours cannot be negative!")
                    elif plant.sunlight_hours < 1:
                        raise ValueError(f"Error checking {plant.name}: \
Sunlight hours {plant.sunlight_hours} is too low (min 2)")
                    else:
                        raise ValueError(f"Error checking {plant.name}: \
Sunlight hours {plant.sunlight_hours} is too high (max 12)")
                else:
                    print(f"{plant.name}: healthy (water: \
{plant.water_level}, sun: {plant.sunlight_hours})")
            except ValueError as e:
                print(e)

    def check_tank_validity(self):
        """
        This function checks the validity of the tank of a garden.

        Raises:
            WaterError: If the water level of the tank is lower than 200L
        """
        try:
            if self.water_tank.water < 200:
                raise WaterError("Not enough water in tank")
            else:
                print("Tank is valid")
        except GardenError as e:
            print(f"Caught GardenError: {e}")


def test_garden_management() -> None:
    """
    This function demonstrates that the GardenManager class works
    and manages errors properly.
    """
    garden = GardenManager([], Tank(199))
    print("Adding plants to garden...")
    garden.add_plant(Plant("tomato", 5, 8))
    garden.add_plant(Plant("lettuce", 15, 7))
    garden.add_plant(Plant("potato", 6, 17))
    garden.add_plant(Plant("", 5, 5))
    print("")
    print("Watering plants...")
    garden.water_plants()
    print("")
    print("Checking plant health...")
    garden.check_plants_health()
    print("")
    print("Testing error recovery...")
    garden.check_tank_validity()
    print("System recovered and continuing")


# --- Tests and Main program ---
if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()
    print("\nGarden management system test complete!")
