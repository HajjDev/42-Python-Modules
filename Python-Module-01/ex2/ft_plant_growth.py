#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 14:22:45 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 16:36:52 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# --- Main Plant Class ---
class Plant:
    """
    This class represents an object that is a plant.
    A plant can have many attributes, of wich a name, a height and an age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        The __init__ function initializes the Plant object with the following
        attributes.

        Args:
            name (str): The name of the plant
            height (int): The height of the plant
            age (int): The age of the plant
        """
        self.name = name
        self.height = height
        self.current_age = age

    def grow(self) -> None:
        """
        This function increments the plants height by one.
        """
        self.height += 1

    def age(self) -> None:
        """
        This function increments the plants age by one.
        """
        self.current_age += 1

    def get_info(self) -> str:
        """
        This function let's us gather the information of the corresponding
        plant. We'll receive it's name, it's height and it's age.

        Returns:
            str: The information of the plant in the form:
            (Plant name): (Plant height)cm, (Plant age) days old
        """
        return f"{self.name}: {self.height}cm, {self.current_age} days old"


# --- Main Program ---
if __name__ == "__main__":
    # --- Basic Tests ---
    rose = Plant("Rose", 25, 30)
    rose_height = rose.height

    print("=== Day 1 ===")
    print(rose.get_info())
    for i in range(0, 6):
        rose.grow()
        rose.age()
    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Grow this week: +{rose.height - rose_height}")

    # --- Additional Tests ---
    # print("")
    # plants = [Plant("Tulipe", 13, 70), Plant("Sunflower", 80, 45),
    #           Plant("Cactus", 15, 120)]
    # for plant in plants:
    #     current_height = plant.height
    #     print("=== Day 1 ===")
    #     print(plant.get_info())
    #     for i in range(0, 13):
    #         plant.grow()
    #         plant.age()
    #     print("=== Day 14 ===")
    #     print(plant.get_info())
    #     print(f"Grow this week: +{plant.height - current_height}")
    #     print("")
