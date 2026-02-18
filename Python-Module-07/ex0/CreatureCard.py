# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CreatureCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 07:38:48 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 14:18:31 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card


class CreatureCard(Card):
    """
    This class represents a special type of card, Creatures. Creatures can
    attack other card and have a huge amount of health.
    """
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        """
        This function initializes the card with the following
        attributes.

        Args:
            name (str): The name of the card.
            cost (int): The price to play the card.
            rarity (str): The rarity of the card.
            attack (int): The damage of the card.
            health (int): The health of the card

        Raises:
            ValueError: Raises a ValueError if the health or attack
            is negative.
        """
        super().__init__(name, cost, rarity)
        if (not isinstance(attack, int) or attack < 0 or
                not isinstance(health, int) or health < 0):
            raise ValueError("Attack and Health must be positive integers")
        self.attack = attack
        self.health = health
        self.data_type = "creatures"
        self.type = "Creature"

    def play(self, game_state: dict) -> dict:
        """
        This function plays the card in the current turn.

        Args:
            game_state (dict): The state of the game (number of
            mana available).

        Returns:
            dict: A dictionary containing the information of the turn.
        """
        if self.is_playable(game_state["available_mana"]):
            print("Playable: True")
            play_results = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }
            game_state["available_mana"] -= self.cost
            return play_results
        else:
            print("Playable: False")
            return {}

    def attack_target(self, target) -> dict:
        """
        This function attacks a specific target with the amount
        of damage of the card.

        Args:
            target (_type_): The target to attack.

        Returns:
            dict: A dictionary containing information about the
            attack (Attacker, target, damage dealt).
        """
        if hasattr(target, "health"):
            attack_results = {
                "attacker": self.name,
                "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": True
            }
            target.health -= self.attack
            if target.health < 0:
                target.health = 0
            return attack_results
        else:
            print("Target Not Valid")
            return {}
