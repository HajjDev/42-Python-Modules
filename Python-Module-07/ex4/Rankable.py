# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Rankable.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 12:02:23 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 15:00:15 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class Rankable(ABC):
    """
    This class represents a special type of card that can be ranked according
    to it's rating.
    """
    @abstractmethod
    def calculate_rating(self) -> int:
        """
        This function calculates the rating of the current card
        based on all of it's previous matches.

        Returns:
            int: The calculated rating.
        """
        ...

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        This function increments the wins of the current card.

        Args:
            wins (int): The number of wins to be added.
        """
        ...

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        This function increments the losses of the current card.

        Args:
            wins (int): The number of losses to be added.
        """
        ...

    @abstractmethod
    def get_rank_info(self) -> dict:
        """
        This function gives the number of wins and losses of
        the current card.

        Returns:
            dict: A dictionary containing the information mentioned
            above.
        """
        ...
