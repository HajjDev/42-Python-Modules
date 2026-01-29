#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_gardent_data.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.42belgium.be   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 14:12:46 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 00:33:27 by cel-hajj        ###   ########.fr        #
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


# --- Main Program ---
if __name__ == "__main__":
    # --- Basic Tests ---
    plants = [Plant("Rose", 25, 30), Plant("Sunflower", 80, 45),
              Plant("Cactus", 15, 120)]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.current_age} days old")

    # --- Additional Tests ---
#     print("")
#     plants = [Plant("Tulipe", 15, 10), Plant("Lilies", 90, 35),
#               Plant("Daisies", 17, 20)]
#     for plant in plants:
#         print(f"{plant.name}: {plant.height}cm, {plant.current_age} \
# days old")
