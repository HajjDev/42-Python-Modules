# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CardFactory.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 08:03:11 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 14:50:40 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """
    This class represents a factory cards that can create any type of card but
    also create themed decks.
    """
    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """
        This function creates a Creature card.

        Args:
            name_or_power (str | int | None, optional): The name of the
            creature or the amount of damage it does. Defaults to None.

        Returns:
            Card: The newly created card.
        """
        ...

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """
        This function creates a Spell card.

        Args:
            name_or_power (str | int | None, optional): The name of the
            spell or the damage/heal it does. Defaults to None.

        Returns:
            Card: The newly created card.
        """
        ...

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """
        This function creates an Artifact card.

        Args:
            name_or_power (str | int | None, optional): The name of the
            artifact or the effect number of it. Defaults to None.

        Returns:
            Card: The newly created card.
        """
        ...

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """
        This function creates a themed deck, with different types
        of cards that point to the same theme.

        Args:
            size (int): The size of the deck.

        Returns:
            dict: A dictionary containing the cards part of the deck.
        """
        ...

    @abstractmethod
    def get_supported_types(self) -> dict:
        """
        This function highlights the types supported by the factory.

        Returns:
            dict: A dictionary containing the types supported by
            the factory.
        """
        ...
