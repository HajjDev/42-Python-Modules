#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 17:48:21 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 16:36:57 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# --------------------
# --- Plant System ---
# --------------------

# --- Main Plant Class ---
class Plant:
    """
    This class represents an object that is a plant.
    A plant can have many attributes, of wich a name and a height.
    """
    def __init__(self, name: str, height: int) -> None:
        """
        The __init__ function initializes the Plant object with the following
        attributes.

        Args:
            name (str): The name of the plant
            height (int): The height of the plant
        """
        self.name = name
        self.height = height

    def grow(self, centimeters: int):
        """
        This function increments the height of the plant.

        Args:
            centimeters (int): The amount of height to be added.
        """
        self.height += 1
        print(f"{self.name} grew {centimeters}cm")

    def __str__(self) -> str:
        """
        This function displays the information of the plant when we print it
        on the console.
        This function is not to be called, it is automatically executed when
        print() is used.

        Returns:
            str: Information of the plant in the form:
            (Plant name): (Plant height)cm
        """
        return f"{self.name}: {self.height}cm"


# --- FloweringPlant class inherating from Plant ---
class FloweringPlant(Plant):
    """
    This class represents an object that is a plant that flowers.
    A flowering plant can have many attributes, of wich a name, a height and
    a color.
    """
    def __init__(self, name: str, height: int, color: str) -> None:
        """
        The __init__ function initializes the FloweringPlant object with the
        following attributes using it's mother class __init__ method.

        Args:
            name (str): The name of the flowering plant
            height (int): The height of the flowering plant
            color (str): The color of the flowering plant
        """
        super().__init__(name, height)
        self.color = color

    def __str__(self) -> str:
        """
        This function displays the information of the flowering plant when we
        print int on the console.
        This function is not to be called, it is automatically executed when
        print() is used.

        Returns:
            str: Information of the plant in the form:
            (FloweringPlant name): (FloweringPlant height)cm,
            (FloweringPlant color) (blooming)
        """
        return f"{super().__str__()}, {self.color} color (blooming)"


# --- PrizeFlower class inherating from FloweringPlant ---
class PrizeFlower(FloweringPlant):
    """
    This class represents an object that is a flowering plant with a prize.
    A prize flower can have many attributes, of wich a name, a height,
    a color and prize points.
    """
    def __init__(self, name: str, height: int, color: str,
                 prize_points: int) -> None:
        """
        The __init__ function initializes the PrizeFlower object with the
        following attributes using it's mother class __init__ method.

        Args:
            name (str): The name of the prize flower
            height (int): The height of the prize flower
            color (str): The color of the prize flower
            prize_points (int): The prize points of the prize flower
        """
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        """
        This function displays the information of the prize flower when we
        print int on the console.
        This function is not to be called, it is automatically executed when
        print() is used.

        Returns:
            str: Information of the plant in the form:
            (PrizeFlower name): (PrizeFlower height)cm, (PrizeFlower color)
            (blooming), Prize points: (PrizeFlower prize points)
        """
        return f"{super().__str__()}, Prize points: {self.prize_points}"


# ----------------------------
# --- GardenManager System ---
# ----------------------------

class GardenManager:
    """
    This class manages the garden of an owner, each garden has a set of plants
    that can grow.
    """
    def __init__(self, owner: str) -> None:
        """
        The __init__ function initializes the Plant object with the following
        attributes.

        Args:
            owner (str): the owner of the garden
        """
        self.owner = owner
        self.plants: list[Plant] = []
        self.total_plant_growth = 0

    def add_plant_to_garden(self, plant: Plant) -> None:
        """
        This function adds a plant to the garden.

        Args:
            plant (Plant): The plant to be added
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    @classmethod
    def create_garden_network(cls, owner: str,
                              plants: list[Plant]) -> "GardenManager":
        """
        This function creates a garden network by adding plants
        to the garden of it's owner.

        Args:
            owner (str): The owner of the garden.
            plants (list[Plant]): The plants to be added to the garden

        Returns:
            GardenManager: A new garden assigned to this owner along
            with all the plants.
        """
        garden = cls(owner)
        for plant in plants:
            garden.add_plant_to_garden(plant)
        return garden

    def grow_all_plants(self, centimeters: int) -> None:
        """
        This function grows the plants in the garden by a certain
        amount of height.

        Args:
            centimeters (int): The amount of height to be added
        """
        print(f"{self.owner} is helping all plants grow")
        for plant in self.plants:
            self.total_plant_growth += 1
            plant.grow(centimeters)

    def get_garden_report(self) -> None:
        """
        This function displays a total report of the current garden.
        A total report contains:
            - The total number of plants available
            - The total amount of growth
            - The information on each plant type
            - The height validation test
        """
        total_plants = self.GardenStats.get_total_plants(self.plants)
        total_heights = [self.GardenStats.positive(plant.height)
                         for plant in self.plants]
        total_plant_types = self.GardenStats.get_garden_types(self.plants)

        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")
        print("")
        print(f"Plants added: {total_plants}, Total growth: \
{self.total_plant_growth}cm")
        print(f"Plant types: {total_plant_types['r']} regular, \
{total_plant_types['f']} flowering, {total_plant_types['p']} prize flowers")
        print("")
        print(f"Height validation test: {False not in total_heights}")

    def get_garden_score(self) -> int:
        """
        This function calculates the total score of the garden.
        The score of a garden is represented by the sum of the heights of
        it's plants.

        Returns:
            int: The score of the current garden
        """
        return self.GardenStats.get_garden_score(self.plants)

    class GardenStats:
        """
        This class is a helper class defined to calculate the statistics
        of a garden. Including the total amount of plants, the total amount by
        type, valid heights, the total score of a garden and other utility
        functions.
        """
        @staticmethod
        def get_total_plants(plants: list[Plant]) -> int:
            """
            This function calculates the number of plants in a list
            of plants.

            Args:
                plants (list[Plant]): The list containing the plants

            Returns:
                int: The number of plants in the list.
            """
            total_plants = 0
            for _ in plants:
                total_plants += 1
            return total_plants

        @staticmethod
        def positive(number: int) -> bool:
            """
            This method checks weither a number is positive / null or not.

            Args:
                number (int): The number to be checked

            Returns:
                bool: True if the number is positive or null, False otherwise
            """
            if (number < 0):
                return False
            return True

        @staticmethod
        def get_garden_score(plants: list[Plant]) -> int:
            """
            This method calculates the score of a list of plants.

            Args:
                plants (list[Plant]): The list of the plants of a garden

            Returns:
                int: The score of the garden.
            """
            score = 0
            for plant in plants:
                score += plant.height
            return score

        @staticmethod
        def get_garden_types(plants: list[Plant]) -> dict[str, int]:
            """
            This function calculates the amount of plants by type.

            Args:
                plants (list[Plant]): The list of the plants of a garden

            Returns:
                dict[str, int]: A dictionnary containing the number of each
                type respectively. (Regular, flowering or prize flower)
            """
            plants_data = {'r': 0, 'f': 0, 'p': 0}
            for plant in plants:
                if (plant.__class__.__name__ == "Plant"):
                    plants_data['r'] += 1
                elif (plant.__class__.__name__ == "FloweringPlant"):
                    plants_data['f'] += 1
                elif (plant.__class__.__name__ == "PrizeFlower"):
                    plants_data['p'] += 1
            return plants_data


# --- Main Program ---
if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print("")
    plants: list[Plant] = [Plant("Oak Tree", 100),
                           FloweringPlant("Rose", 25, "red"),
                           PrizeFlower("Sunflower", 50, "yellow", 10)]
    gardens: list[GardenManager] = []
    total_gardens = 0
    alice_garden = GardenManager.create_garden_network("Alice", plants)
    print("")
    bob_garden = GardenManager("Bob")
    gardens.append(alice_garden)
    total_gardens += 1
    gardens.append(bob_garden)
    total_gardens += 1

    alice_garden.grow_all_plants(1)
    print("")
    alice_garden.get_garden_report()
    garden_scores = ""
    for garden in gardens:
        if garden != gardens[-1]:
            garden_scores += f"{garden.owner}: {garden.get_garden_score()}, "
        else:
            garden_scores += f"{garden.owner}: {garden.get_garden_score()}"
    print(f"Garden scores - {garden_scores}")
    print(f"Total gardens managed: {total_gardens}")
