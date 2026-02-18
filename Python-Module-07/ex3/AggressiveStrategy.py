# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AggressiveStrategy.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 08:03:06 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 14:45:56 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """
    This class represents a special type of Strategy. AggressiveStrategies
    consists of strategies to attack enemies.
    """
    def __init__(self):
        """
        This function initializes the strategy with a name and an empty list
        of targets to prioritize.
        """
        self.name = "AggressiveStrategy"
        self.prioritized_targets = []

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
        try:
            actions = {
                "cards_played": [],
                "mana_used": 0,
                "targets_attacked": [],
                "damage_dealt": 0
            }
            for h in hand:
                if h.data_type != "artifacts":
                    actions["cards_played"].append(h.name)
                    actions["mana_used"] += h.cost
                    actions["damage_dealt"] += h.attack
                    if self.prioritized_targets:
                        for enemy in self.prioritized_targets:
                            enemy.health -= (h.attack
                                             if enemy.health - h.attack > 0
                                             else enemy.health)
                        self.prioritized_targets = []
                    for enemy in battlefield:
                        enemy.health -= (h.attack
                                         if enemy.health - h.attack > 0
                                         else enemy.health)
            for enemy in battlefield:
                actions["targets_attacked"].append(enemy.name)
            return actions
        except AttributeError:
            print("Hands are not valid, make sure they are card with the \
attribute damage.")

    def get_strategy_name(self) -> str:
        """
        This function gives the name of the strategy.

        Returns:
            str: The name of the strategy.
        """
        return self.name

    def prioritize_targets(self, available_targets: list) -> list:
        """
        This function prioritizes targets so that in the next turn, they'll
        be the first ones to be attacked.

        Args:
            available_targets (list): The list of targets to prioritize.

        Returns:
            list: A list of the targets.
        """
        for target in available_targets:
            self.prioritized_targets.append(target)
        return self.prioritized_targets
