# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentCard.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 12:02:30 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 15:27:54 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    This class represents a special type of card, a TournamentCard that is
    a combatable and a rankable card.
    """
    def __init__(self, name: str, card_id: str, rating: int,
                 attack: int, health: int):
        """
        This function intializes the card with the following attributes.

        Args:
            name (str): The name of the card.
            card_id (str): The ID of the card.
            rating (int): The base rating of the card.
            attack (int): The damage of the card.
            health (int): The health of the card.
        """
        super().__init__(name, 3, "Legendary")
        self.id = card_id
        self.matches = []
        self.wins = 0
        self.losses = 0
        self.base_rating = rating
        self.attack = attack
        self.health = health
        self.combat_stats = {"attacks": 0, "defends": 0}

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
                "mana_used": self.cost
            }
            game_state["available_mana"] -= self.cost
            return play_results
        else:
            return {}

    def attack(self, target) -> dict:
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
        if hasattr(target, "health"):
            attack_results = {
                "attacker": self.name,
                "target": target.name,
                "damage": self.attack,
                "combat_type": "melee"
            }
            target.health -= self.attack
            if target.health < 0:
                target.health = 0
            self.combat_stats["attacks"] += 1
            return attack_results
        else:
            print("Target Not Valid")
            return {}

    def calculate_rating(self) -> int:
        """
        This function calculates the rating of the current card
        based on all of it's previous matches.

        Returns:
            int: The calculated rating.
        """
        return self.base_rating + sum(self.matches)

    def get_tournament_stats(self) -> dict:
        """
        This function gives the current statistics of the card.
        THe username, the interfaces, the current rating and the
        record.

        Returns:
            dict: A dictionary containing the information mentionned
            above.
        """
        wins = self.wins
        losses = self.losses
        rating = self.calculate_rating()
        return {
            "Username": f"{self.name} (ID: {self.id})",
            "Interfaces": ["Card", "Combatable", "Rankable"],
            "Rating": rating,
            "Record": f"{wins}-{losses}"
        }

    def update_wins(self, wins: int) -> None:
        """
        This function increments the wins of the current card.

        Args:
            wins (int): The number of wins to be added.
        """
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        """
        This function increments the losses of the current card.

        Args:
            wins (int): The number of losses to be added.
        """
        self.losses += losses

    def defend(self, incoming_damage: int) -> dict:
        """
        This function defends the current card from an attack.

        Args:
            incoming_damage (int): The damage of the incoming attack.

        Returns:
            dict: A dictionary containing the whole description of the defense,
            the damage countered, the damage taken and the defender.
        """
        incoming_damage -= 3 if incoming_damage - 3 > 0 else incoming_damage
        if self.health - incoming_damage > 0:
            self.health -= incoming_damage
        else:
            self.health = 0
        defense_results = {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": 3,
            "still_alive": self.health > 0
        }
        self.combat_stats["defends"] += 1
        return (defense_results)

    def get_combat_stats(self) -> dict:
        """
        This function gives the information of all the attacks/defenses
        that the card has done.

        Returns:
            dict: A dictionary containing the number of attacks and defenses.
        """
        return self.combat_stats

    def get_rank_info(self) -> dict:
        """
        This function gives the number of wins and losses of
        the current card.

        Returns:
            dict: A dictionary containing the information mentioned
            above.
        """
        return {
            "wins": self.wins,
            "losses": self.losses
        }
