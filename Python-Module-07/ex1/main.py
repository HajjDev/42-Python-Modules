#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 18:34:10 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 13:31:28 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = Deck()
    game_state = {
        "available_mana": 14
    }
    cards = [
        CreatureCard("Fire Dragon", 5, "Legendary", 7, 5),
        ArtifactCard("Mana Crystal", 2, "Rare", 20, "Permanent: \
+1 mana per turn"),
        SpellCard("Lightning Bolt", 3, "Common", "damage 3")
            ]
    for card in cards:
        deck.add_card(card)
    print(deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")
    deck.shuffle()
    card1 = deck.draw_card()
    print(f"Drew: {card1.name} ({card1.__class__.__name__.split('Card')[0]})")
    print(f"Play result: {card1.play(game_state)}\n")

    card2 = deck.draw_card()
    print(f"Drew: {card2.name} ({card2.__class__.__name__.split('Card')[0]})")
    print(f"Play result: {card2.play(game_state)}\n")

    card3 = deck.draw_card()
    print(f"Drew: {card3.name} ({card3.__class__.__name__.split('Card')[0]})")
    print(f"Play result: {card3.play(game_state)}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")
