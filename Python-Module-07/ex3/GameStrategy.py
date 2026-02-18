# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameStrategy.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 08:03:23 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 14:47:05 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """
    This class represents a GameStrategy. GameStrategies are useful to have a
    better thinking structure in-game.
    """
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        This function executes a full turn with the hands
        being the attackers and the battlefield being
        the enemies

        Args:
            hand (list): The list of attackers.
            battlefield (list): The list of enemies.

        Returns:
            dict: A dictionary containing a report about the battle.
            The attackers, the enemies, the damage_dealt and the status of
            the combat.
        """
        ...

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        This function gives the name of the strategy.

        Returns:
            str: The name of the strategy.
        """
        ...

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """
        This function prioritizes targets so that in the next turn, they'll
        be the first ones to be attacked.

        Args:
            available_targets (list): The list of targets to prioritize.

        Returns:
            list: A list of the targets.
        """
        ...
