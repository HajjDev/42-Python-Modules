# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentPlatform.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 12:02:40 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 15:33:07 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """
    This class represents the platform that can manage a tournament.
    """
    def __init__(self) -> None:
        """
        This function initializes the tournament with no cards and empty
        statistics.
        """
        self.registered_cards = []
        self.matches_played = 0
        self.avg_rating = 0
        self.status = "active"

    def register_card(self, card: TournamentCard) -> str:
        """
        This function adds a new card to the tournament.

        Args:
            card (TournamentCard): The card to be added.

        Returns:
            str: An informational string stating that the card
            has been added.
        """
        self.registered_cards.append(card)
        return f"{card.name} registered."

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """
        This function creates a match between two cards. The rule is
        simple, the card with the most damage wins.

        Args:
            card1_id (str): The first card.
            card2_id (str): The second card.

        Returns:
            dict: A dictionary containing the results of the match.
            The winner, loser, winner rating and loser rating.
        """
        try:
            card1 = None
            card2 = None
            for card in self.registered_cards:
                if card.id == card1_id:
                    card1 = card
                elif card.id == card2_id:
                    card2 = card
            card1_w = card1.attack > card2.attack
            if card1_w:
                card1.update_wins(1)
                card2.update_losses(1)
            else:
                card2.update_wins(1)
                card1.update_losses(1)
            card1.matches.append(16 if card1_w else -16)
            card2.matches.append(16 if not card1_w else -16)
            self.matches_played += 1
            return {
                "winner": card1.id if card1_w else card2.id,
                "loser": card1.id if not card1_w else card2.id,
                "winner_rating": (card1.calculate_rating()
                                  if card1_w else card2.calculate_rating()),
                "loser_rating": (card1.calculate_rating()
                                 if not card1_w else card2.calculate_rating())
            }
        except Exception:
            print("Please, enter valid IDs, or register new cards.")

    def get_leaderboard(self) -> list:
        """
        This function sorts the list of cards based on the rating of
        each card and gives a list of he cards in order.

        Returns:
            list: The list containing the sorted cards.
        """
        sorted_cards = sorted(self.registered_cards,
                              key=lambda card: card.calculate_rating(),
                              reverse=True)
        return sorted_cards

    def generate_tournament_report(self) -> dict:
        """
        This function generates a report about the whole tournament.
        The total cards, matches played, average rating and platform
        status.

        Returns:
            dict: A dictionary containing the information mentionned
            above.
        """
        self.avg_rating = (sum([card.calculate_rating()
                                for card in self.registered_cards])
                           / len(self.registered_cards)
                           if len(self.registered_cards) > 0 else 0)
        return {
            "total_cards": len(self.registered_cards),
            "matches_played": self.matches_played,
            "avg_rating": self.avg_rating,
            "platform_status": self.status
        }
