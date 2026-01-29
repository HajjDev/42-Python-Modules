#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 15:10:58 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 16:36:55 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# --- Main SecurePlant Class ---
class SecurePlant:
    """
    This class represents an object that is a secure plant.
    A plant can have many attributes, of wich a name, a height and an age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        The __init__ function initializes the Plant object with the following
        attributes using private variables.
        This function also checks the parameters value before assigning them.

        Args:
            name (str): The name of the plant
            height (int): The height of the plant
            age (int): The age of the plant
        """
        self.name = name
        # Default values for height and age
        self.__height = 0
        self.__current_age = 0
        print(f"Plant created: {self.name}")
        # Check if height and age are valid before assigning them.
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """
        This function updates the plant's height.
        This function won't modify the height of the plant and
        display an error if the height is negative.

        Args:
            height (int): The new height of the plant
        """
        if (height < 0):
            print(f"Invalid operation attempted: height {height} [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """
        This function updates the plant's age.
        This function won't modify the age of the plant and
        display an error if the age is negative.

        Args:
            age (int): The new age of the plant
        """
        if (age < 0):
            print(f"Invalid operation attempted: age {age} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__current_age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """
        This method gives access to the height of the plant.

        Returns:
            int: The height of the plant.
        """
        return self.__height

    def get_age(self) -> int:
        """
        This method gives access to the age of the plant.

        Returns:
            int: The age of the plant.
        """
        return self.__current_age


# --- Main Program ---
if __name__ == "__main__":
    # --- Basic Tests ---
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print("")
    rose.set_height(-5)
    print(f"Current plant: {rose.name} ({rose.get_height()}cm, \
{rose.get_age()} days)")

    # --- Additional Tests ---
#     print("")
#     tulipe = SecurePlant("Tulipe", 13, 90)
#     print("")
#     tulipe.set_height(24)
#     tulipe.set_age(-10)
#     print("")
#     tulipe.set_age(20)
#     print("")
#     print(f"Current plant: {tulipe.name} ({tulipe.get_height()}cm, \
# {tulipe.get_age()} days)")
