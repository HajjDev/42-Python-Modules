# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Magical.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 07:44:08 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 14:33:10 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class Magical(ABC):
    """
    This class represents a special ability a card can have. It let's the card
    cast spells on other cards but also channel mana onto the game.
    """
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        This function casts a specific spell on some targets.

        Args:
            spell_name (str): The name of the spell.
            targets (list): The targets taking the spell.

        Returns:
            dict: A dictionary containing the information of the casting.
        """
        ...

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """
        This function channels mana onto the game. (Adds mana
        to the turn)

        Args:
            amount (int): The amount of manna to be channeled.

        Returns:
            dict: A dictionary containing the channeled mana and the total
            mana.
        """
        ...

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """
        This function gives us information about the spells the card casted.

        Returns:
            dict: A dictionary containing the number of spells casted by the
            current card.
        """
        ...
