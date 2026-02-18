#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 07:46:30 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/16 08:29:43 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin_warrior = CreatureCard("Goblin Warior", 2, "Common", 3, 1)
    game_stats = {
        "available_mana": 8
    }

    print("CreatureCard info:")
    print(f"{fire_dragon.get_card_info()}\n")

    print(f"Playing Fire Dragon with {game_stats['available_mana']} \
mana available:")
    print(f"Play result: {fire_dragon.play(game_stats)}\n")

    print("Fire Dragon attack Goblin warrior")
    print(f"{fire_dragon.attack_target(goblin_warrior)}\n")

    print(f"Testing insufficient mana ({game_stats['available_mana']} \
available)")
    fire_dragon.play(game_stats)

    print("\nTesting negative health/attack value")
    print("Fire Ant: CreatureCard('Fire Ant', 4, 'Rare', 0, -2)")
    try:
        fire_ant = CreatureCard("Fire Ant", 4, "Rare", 0, -2)
    except ValueError:
        print("Error caught successfully")

    print("\nAbstract pattern successfully demonstrated!")
