# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  SpellCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 18:34:42 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 14:21:43 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card


class SpellCard(Card):
    """
    This class represents a special type of card, Spells. Spells can either
    damage or heal targets.
    """
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        """
        This function initializes the card with the following
        attributes.

        Args:
            name (str): The name of the card.
            cost (int): The price to play the card.
            rarity (str): The rarity of the card.
            effect_type (str): The effect type, (damage or heal).
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.data_type = "spells"
        try:
            self.informations = self.effect_type.split()
            self.attack = (int(self.informations[1])
                           if self.informations[0] == "damage" else 0)
            self.heal = (int(self.informations[1])
                         if self.informations[0] == "heal" else 0)
        except ValueError:
            print("Invalid Spell creation, please provide a number of damage \
or healing")

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
            play_results = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type
            }
            game_state["available_mana"] -= self.cost
            return play_results
        else:
            return {}

    def resolve_effect(self, targets: list) -> dict:
        """
        This function applies the effect of the spell to every
        target in the list.

        Args:
            targets (list): The targets to take the spell.

        Returns:
            dict: A dictionary containing the total amount of damage
            or heal.
        """
        try:
            info = self.effect_type.split()
            points = int(info[1])
            total_points = len(targets) * points
            for target in targets:
                if info[0] == "damage":
                    target.health -= points
                elif info[0] == "heal":
                    target.health += points
            return {
                f"{info[0]} applied": total_points
            }
        except Exception:
            print("Targets not valid, please make sure they are of type Card.")
