# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ArtifactCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 18:34:26 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 14:19:04 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card


class ArtifactCard(Card):
    """
    This class represents a special type of card, Artifacts. Artifacts are like
    charms that can have effects on every turn of the game.
    """
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        """
        This function initializes the card with the following
        attributes.

        Args:
            name (str): The name of the card.
            cost (int): The price to play the card.
            rarity (str): The rarity of the card.
            durability (int): The durability of the card.
            effect (str): The effect of the card.
        """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.data_type = "artifacts"
        self.ability_active = False
        self.total_mana = 0

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
                "effect": self.effect
            }
            game_state["available_mana"] -= self.cost
            self.total_mana += 1 if self.ability_active else 0
            return play_results
        else:
            return {}

    def activate_ability(self) -> dict:
        """
        This function activates the ability of the artifact.

        Returns:
            dict: Aa dictionary containing the benefits of the ability.
        """
        print(f"Ability activated: {self.effect}")
        self.ability_active = True
        return {"mana_generated": 1, "total_mana": self.total_mana}
