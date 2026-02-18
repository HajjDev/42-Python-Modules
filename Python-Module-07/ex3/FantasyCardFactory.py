# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  FantasyCardFactory.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 08:03:17 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 14:52:07 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """
    """
    def __init__(self) -> None:
        """
        This function initializess the factory with an empty list
        of cards and empty amounts of each special type.
        """
        self.cards = []
        self.creature_count = 0
        self.artifact_count = 0
        self.spell_count = 0

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """
        This function creates a Creature card.

        Args:
            name_or_power (str | int | None, optional): The name of the
            creature or the amount of damage it does. Defaults to None.

        Returns:
            Card: The newly created card.
        """
        if isinstance(name_or_power, str):
            creature = CreatureCard(name_or_power, 3, "Common", 4, 10)
        elif isinstance(name_or_power, int):
            creature = CreatureCard(f"Creature {self.creature_count}",
                                    name_or_power, "Common", 4, 10)
            self.creature_count += 1
        else:
            creature = CreatureCard(f"Creature {self.creature_count}",
                                    2, "Common", 4, 10)
            self.creature_count += 1
        self.cards.append(creature)
        return creature

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """
        This function creates a Spell card.

        Args:
            name_or_power (str | int | None, optional): The name of the
            spell or the damage/heal it does. Defaults to None.

        Returns:
            Card: The newly created card.
        """
        if isinstance(name_or_power, str):
            spell = SpellCard(name_or_power, 3, "Rare", "damage 3")
        elif isinstance(name_or_power, int):
            spell = SpellCard(f"Spell {self.spell_count}", 3,
                              "Rare", f"damage {name_or_power}")
            self.spell_count += 1
        else:
            spell = SpellCard(f"Spell {self.spell_count}", 3,
                              "Rare", "damage 2")
            self.spell_count += 1
        self.cards.append(spell)
        return spell

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """
        This function creates an Artifact card.

        Args:
            name_or_power (str | int | None, optional): The name of the
            artifact or the effect number of it. Defaults to None.

        Returns:
            Card: The newly created card.
        """
        if isinstance(name_or_power, str):
            arti = ArtifactCard(name_or_power, 2, "Legendary", 3,
                                "Permanent: +1 mana per turn")
        elif isinstance(name_or_power, int):
            arti = ArtifactCard(f"Artifact {self.artifact_count}", 2,
                                "Legendary", 3,
                                f"Permanent: +{name_or_power} mana per turn")
            self.artifact_count += 1
        else:
            arti = ArtifactCard(f"Artifact {self.artifact_count}", 2,
                                "Legendary", 3, "Permanent: +2 mana per turn")
            self.artifact_count += 1
        self.cards.append(arti)
        return arti

    def create_themed_deck(self, size: int) -> dict:
        """
        This function creates a themed deck, with different types
        of cards that point to the same theme.

        Args:
            size (int): The size of the deck.

        Returns:
            dict: A dictionary containing the cards part of the deck.
        """
        themed_deck = {
            "creatures": 0,
            "spells": 0,
            "artifacts": 0
        }
        for i in range(size):
            card_creator = random.choice([
                self.create_artifact,
                self.create_creature,
                self.create_spell
            ])
            card = card_creator()
            themed_deck[card.data_type] += 1
        return themed_deck

    def get_supported_types(self) -> dict:
        """
        This function highlights the types supported by the factory.

        Returns:
            dict: A dictionary containing the types supported by
            the factory.
        """
        return {'creatures': ['dragon', 'goblin'],
                'spells': ['fireball'],
                'artifacts': ['mana_ring']
                }
