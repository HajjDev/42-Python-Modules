# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Combatable.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 07:44:03 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 14:30:11 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from ex0.Card import Card


class Combatable(ABC):
    """
    This class represents a special ability a card can have. It let's the card
    attack other cards and also defend itself from other attacks.
    """
    @abstractmethod
    def attack(self, target: Card) -> dict:
        """
        This function attacks the target with the amount
        of damage of the following card.

        Args:
            target (Card): The target to be attacked.

        Returns:
            dict: A dictionary containing the whole description
            of the attack. The attack, defender, amount of damage dealt and
            the status of the defender.
        """
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """
        This function defends the current card from an attack.

        Args:
            incoming_damage (int): The damage of the incoming attack.

        Returns:
            dict: A dictionary containing the whole description of the defense,
            the damage countered, the damage taken and the defender.
        """
        ...

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """
        This function gives the information of all the attacks/defenses
        that the card has done.

        Returns:
            dict: A dictionary containing the number of attacks and defenses.
        """
        ...
