#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 08:03:56 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 13:48:47 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===\n")

    game_engine = GameEngine()
    factory = FantasyCardFactory()
    factory.create_themed_deck(8)
    aggressive_strat = AggressiveStrategy()
    game_engine.configure_engine(factory, aggressive_strat)
    print(f"""Configuring Fantasy Card Game...
Factory: FantasyCardFactory
Strategy: AggressiveStrategy
Available types: {factory.get_supported_types()}\n""")

    print("Simulating agressive turn...")
    print(f"Hand: \
{[f'{h.name} ({h.attack})' for h in factory.cards if h.type != 'artifacts']}")

    print("""\nTurn execution:
Strategy: AgressiveStrategy""")
    print(f"Actions: {game_engine.simulate_turn()}\n")

    print("Game Report:")
    print(f"{game_engine.get_engine_status()}\n")

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
