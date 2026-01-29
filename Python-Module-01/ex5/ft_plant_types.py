#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.42belgium.be   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 17:11:04 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 00:48:31 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# --- Main PLant Class ---
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

    def __str__(self) -> str:
        """
        This function displays the information of the plant when we print it
        on the console.
        This function is not to be called, it is automatically executed when
        print() is used.

        Returns:
            str: Information of the plant in the form:
            (Plant name) (Type of the Plant): (Plant height)cm,
            (Plant age) days
        """
        return f"{self.name} ({self.__class__.__name__}): {self.height}cm, \
{self.current_age} days"


# --- Flower class inherating from Plant ---
class Flower(Plant):
    """
    This class represents an object that is a plant, but of type flower.
    A flower can have many attributes, of wich a name, a height, an age and a
    color.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        The __init__ function initializes the Flower object with the following
        attributes using it's mother class __init__ method.

        Args:
            name (str): The name of the flower
            height (int): The height of the flower
            age (int): The age of the flower
            color (str): The color of the flower
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """
        This function when called, displays a message about the flower
        blooming.
        """
        print(f"{self.name} is blooming beautifully!")

    def __str__(self) -> str:
        """
        This function displays the information of the flower when we print it
        on the console. This function also uses the __str__ method of it's
        mother class but with a string added.

        This function is not to be called, it is automatically executed when
        print() is used.

        Returns:
            str: Information of the flower in the form:
            (Plant name) (Type of the Plant): (Plant height)cm,
            (Plant age) days, (Plant color) color
        """
        return f"{super().__str__()}, {self.color} color"


# --- Tree class inherating from Plant ---
class Tree(Plant):
    """
    This class represents an object that is a plant, but of type tree.
    A tree can have many attributes, of wich a name, a height, an age and a
    trunk diameter.
    """
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """
        The __init__ function initializes the Tree object with the following
        attributes using it's mother class __init__ method.

        Args:
            name (str): The name of the tree
            height (int): The height of the tree
            age (int): The age of the tree
            trunk_diameter (int): The trunk diameter of the tree
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """
        This function displays on the screen the shade of the tree.
        """
        print(f"{self.name} provides {self.trunk_diameter} square meters of \
shade")

    def __str__(self) -> str:
        """
        This function displays the information of the tree when we print it
        on the console. This function also uses the __str__ method of it's
        mother class but with a string added.

        This function is not to be called, it is automatically executed when
        print() is used.

        Returns:
            str: Information of the tree in the form:
            (Tree name) (Type of the Tree): (Tree height)cm,
            (Tree age) days, (Tree trunk diameter)cm diameter
        """
        return f"{super().__str__()}, {self.trunk_diameter}cm diameter"


# --- Vegetable class inherating from Plant ---
class Vegetable(Plant):
    """
    This class represents an object that is a plant, but of type vegetable.
    A vegetable can have many attributes, of wich a name, a height, an age, a
    harvest season and a nutritional value.
    """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        The __init__ function initializes the Vegetable object with the
        following attributes using it's mother class __init__ method.

        Args:
            name (str): The name of the vegetable
            height (int): The height of the vegetable
            age (int): The age of the vegetable
            harvest_season (str): The harvest season of the vegetable
            nutritional_value (str): The nutritional value of the vegetable
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_val = nutritional_value

    def nutritional_value(self) -> None:
        """
        This function displays the nutritional value of the vegetable.
        """
        print(f"{self.name} is rich in vitamin {self.nutritional_val}")

    def __str__(self) -> str:
        """
        This function displays the information of the vegetable when we print
        it on the console. This function also uses the __str__ method of it's
        mother class but with a string added.

        This function is not to be called, it is automatically executed when
        print() is used.

        Returns:
            str: Information of the vegetable in the form:
            (Vegetable name) (Type of the Vegetable): (Vegetable height)cm,
            (Vegetable age) days, (Vegetable harvest season) season
        """
        return f"{super().__str__()}, {self.harvest_season} harvest"


# --- Main Program ---
if __name__ == "__main__":
    # --- Basic Tests ---
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    print(rose)
    rose.bloom()
    print(" ")

    oak = Tree("Oak", 500, 1825, 50)
    print(oak)
    oak.produce_shade()
    print(" ")

    tomato = Vegetable("Tomato", 80, 90, "summer", "C")
    print(tomato)
    tomato.nutritional_value()
    print(" ")

    # --- Additional Tests ---
    # tulipe = Flower("Tulipe", 15, 10, "white")
    # print(tulipe)
    # tulipe.bloom()
    # print(" ")

    # pine = Tree("Pine", 800, 2021, 80)
    # print(pine)
    # pine.produce_shade()
    # print(" ")

    # potato = Vegetable("Potato", 10, 100, "winter", "D")
    # print(potato)
    # potato.nutritional_value()
    # print(" ")
