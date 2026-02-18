# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Card.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 07:32:13 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 14:13:38 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class Card(ABC):
    """
    This class represents a Card model that can be played in a regular match
    of cards.
    """
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """
        This function initializes the class with the following
        attributes.

        Args:
            name (str): The name of the card.
            cost (int): The price to play the card.
            rarity (str): The rarity of the card.
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        This function plays the card in the current turn.

        Args:
            game_state (dict): The state of the game (number of
            mana available).

        Returns:
            dict: A dictionary containing the information of the turn.
        """
        ...

    def get_card_info(self) -> dict:
        """
        This function gives some information about the card.

        Returns:
            dict: A dictionary containing all of the attributes of
            the card and their values.
        """
        card_info = {}
        for name, value in self.__dict__.items():
            if name != "data_type":
                card_info[name] = value
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        """
        This functions checks whether the card is playable,
        so if there eis enough mana to play the card.

        Args:
            available_mana (int): The mana available.

        Returns:
            bool: True if there is enough mana, False otherwise.
        """
        return available_mana >= self.cost
