# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  EliteCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 07:44:05 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 14:36:23 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    """
    This class represents a special attribute a card can have, a card of this
    type if Combatable (able to attack and defend) and Magical (able to cast
    spells and channel mana).
    """
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        """
        This function initializes the card with the following attributes.

        Args:
            name (str): The name the of the card.
            cost (int): The price to play the card.
            rarity (str): The rarity of the card.
            attack (int): The damage caused by the card.
            health (int): The health of the card.
        """
        super().__init__(name, cost, rarity)
        self.attack_damage = attack
        self.combat_stats = {"attacks": 0, "defends": 0}
        self.magic_stats = {"casts": 0}
        self.health = health
        self.mana_pool = 0

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
                "damage": self.attack_damage,
                "combat_type": "melee"
            }
            target.health -= self.attack_damage
            if target.health < 0:
                target.health = 0
            self.combat_stats["attacks"] += 1
            return attack_results
        else:
            print("Target Not Valid")
            return {}

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
        return defense_results

    def get_combat_stats(self) -> dict:
        """
        This function gives the information of all the attacks/defenses
        that the card has done.

        Returns:
            dict: A dictionary containing the number of attacks and defenses.
        """
        return self.combat_stats

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        This function casts a specific spell on some targets.

        Args:
            spell_name (str): The name of the spell.
            targets (list): The targets taking the spell.

        Returns:
            dict: A dictionary containing the information of the casting.
        """
        try:
            spell_cast = {
                "caster": self.name,
                "spell": spell_name,
                "targets": [t.name for t in targets],
                "mana_used": len(targets) * self.cost
            }
            for target in targets:
                target.health -= 3 if target.health - 3 > 0 else target.health
            self.magic_stats["casts"] += 1
            return spell_cast
        except AttributeError:
            return {"error": "Targets Error"}

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
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }

    def get_magic_stats(self) -> dict:
        """
        This function gives us information about the spells the card casted.

        Returns:
            dict: A dictionary containing the number of spells casted by the
            current card.
        """
        return self.magic_stats
