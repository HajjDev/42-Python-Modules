# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Deck.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 18:34:40 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 14:25:24 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random
from ex0.Card import Card


class Deck:
    """
    This class represents a deck of cards. A deck can contain multiple type
    of cards.
    """
    def __init__(self) -> None:
        """
        This function initializes the deck with an empty list of cards and a
        dictionary of informations.
        """
        self.cards = []
        self.deck_stats = {
            "total_cards": 0,
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0
        }

    def add_card(self, card: Card) -> None:
        """
        This function adds a card to the deck.

        Args:
            card (Card): The card to be added.
        """
        self.cards.append(card)
        self.deck_stats[card.data_type] += 1

    def remove_card(self, card_name: str) -> bool:
        """
        This function removes a specific card from the deck.

        Args:
            card_name (str): The name of the card that needs to
            be removed.

        Returns:
            bool: True if the card has been removed, False otherwise.
        """
        card_names = [c.name for c in self.cards]
        if card_name in card_names:
            card = self.cards[card_names.index(card_name)]
            self.deck_stats[card.data_type] -= 1
            self.cards.remove(card)
            return True
        else:
            return False

    def shuffle(self) -> None:
        """
        This functions shuffles the deck of cards.
        """
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """
        This function draws the last card of the deck.

        Returns:
            Card: The drawn card.
        """
        if not self.cards:
            return None
        card = self.cards.pop()
        self.deck_stats[card.data_type] -= 1
        return card

    def get_deck_stats(self) -> dict:
        """
        This function gives the statistics of the deck. The number of cards,
        the average cost of each card and  the number of special cards.

        Returns:
            dict: The dictionary containing all of the information above.
        """
        self.deck_stats["total_cards"] = len(self.cards)
        self.deck_stats["avg_cost"] = (
            sum([c.cost for c in self.cards]) / len(self.cards)
            if len(self.cards) != 0 else 0
        )
        return self.deck_stats
