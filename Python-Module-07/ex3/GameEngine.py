# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameEngine.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 08:03:20 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 14:57:28 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """
    """
    def __init__(self) -> None:
        """
        This function initializes the Engine with no factory, no strategy and
        empty statistics.
        """
        self.factory = None
        self.strategy = None
        self.status = {
            "turns_simulated": 0,
            "total_damage": 0,
            "strategy_used": "AggressiveStrategy",
            "cards_created": 0,
        }

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """
        This function configures the engine by assigning a factory
        and a strategy to it.

        Args:
            factory (CardFactory): The factory to be assigned to the current
            engine.
            strategy (GameStrategy): The strategy to be assigned to the current
            engine.
        """
        self.strategy = strategy
        self.factory = factory

    def simulate_turn(self) -> dict:
        """
        This function simulates a full turn by creating new cards if the
        factory is empty and executing a turn with the existing cards /
        created cards.

        Returns:
            dict: A dictionary containing a report about the battle.
            The attackers, the enemies, the damage_dealt and the status of
            the combat.
        """
        try:
            self.status["turns_simulated"] += 1
            hand = self.factory.cards
            if hand == []:
                self.factory.create_themed_deck(8)
            battlefield = [self.factory.create_creature(),
                           self.factory.create_creature()]
            turn_info = self.strategy.execute_turn(hand, battlefield)
            self.status["total_damage"] += turn_info["damage_dealt"]
            self.status["cards_created"] += len(self.factory.cards)
            return turn_info
        except Exception:
            print("Please, make sure to configure the Engine before using it.")
            return {"damage_dealt": 0, "cards_played": []}

    def get_engine_status(self) -> dict:
        """
        This function gives the status of the Engine (turns simulated,
        total damage, strategy used and the number of cards).

        Returns:
            dict: A dictionary containing all of the information mentioned
            above.
        """
        return self.status
