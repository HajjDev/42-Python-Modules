#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 14:59:26 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 16:36:53 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# --- Main Plant Class ---
class Plant:
    """
    This class represents an object that is a plant.
    A plant can have many attributes, of wich a name, a height and an age.
    """
    # This variable let's us store the amount of plants we created.
    total_plants = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        The __init__ function initializes the Plant object with the following
        attributes.
        This function also increases the amount of total plants and displays a
        message when the plant is created.

        Args:
            name (str): The name of the plant
            height (int): The height of the plant
            age (int): The age of the plant
        """
        self.name = name
        self.height = height
        self.current_age = age
        Plant.total_plants += 1
        print(f"Created: {self.name} ({self.height}cm, \
{self.current_age} days)")


# --- Main Program ---
if __name__ == "__main__":
    # --- Basic Tests ---
    print("=== Plant Factory Output")
    plants = [Plant("Rose", 25, 30), Plant("Sunflower", 80, 45),
              Plant("Cactus", 15, 120)]
    print(f"Total plants created: {Plant.total_plants}")

    # --- Additional Tests ---
    # print("")
    # plants_additional = [Plant("Tulipe", 5, 40),
    #                      Plant("Lilies", 60, 25), Plant("Daisies", 75, 130)]
    # print(f"Total plants created: {Plant.total_plants}")
