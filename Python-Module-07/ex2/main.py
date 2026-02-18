#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/17 07:44:21 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 00:07:55 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex2.EliteCard import EliteCard


if __name__ == "__main__":
    print("=== DataDeck Ability System ===\n")

    print("""EliteCard capabilities:
- Card: ['play', 'get_card_info', 'is_playable']
- Combatable: ['attack', 'defend', 'get_combat_stats']
- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n""")

    print("Playing Arcane Warrior (Elite Card):\n")
    arcane_warrior = EliteCard("Arcane Warrior", 2, "Legendary", 5, 50)

    print("Combat phase:")
    enemy = EliteCard("Enemy", 1, "Common", 3, 8)
    print(arcane_warrior.attack(enemy))
    print(arcane_warrior.defend(5))

    print("\nMagic phase:")
    enemy1 = EliteCard("Enemy1", 1, "Common", 3, 8)
    enemy2 = EliteCard("Enemy2", 1, "Common", 3, 8)
    print(arcane_warrior.cast_spell("Fireball", [enemy1, enemy2]))
    print(arcane_warrior.channel_mana(3))

    print("\nMultiple interface implementation successful!")
