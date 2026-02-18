#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 12:02:15 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/18 13:47:38 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===\n")
    tournament = TournamentPlatform()
    fire_dragon = TournamentCard("Fire Dragon", "dragon_001", 1200, 10, 8)
    ice_wizard = TournamentCard("Ice Wizard", "wizard_001", 1150, 5, 3)

    cards = [fire_dragon, ice_wizard]
    print("Registering Tournament Cards...\n")
    tournament.register_card(fire_dragon)
    tournament.register_card(ice_wizard)
    for card in cards:
        info = card.get_tournament_stats()
        print(f"""{info["Username"]}:
- Interfaces: {info["Interfaces"]}
- Rating: {info["Rating"]}
- Record: {info["Record"]}
""")

    print("Creating tournament match...")
    match = tournament.create_match("dragon_001", "wizard_001")
    match2 = tournament.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match}\n")
    print(f"Match2 result: {match2}\n")

    print("Tournament Leaderboard:")
    leaderboard = tournament.get_leaderboard()
    for i in range(len(leaderboard)):
        data = leaderboard[i]
        print(f"{i + 1}. {data.name} - Rating: {data.calculate_rating()} \
({data.wins}-{data.losses})")

    print("\nPlatform Report:")
    print(f"{tournament.generate_tournament_report()}\n")

    print("""=== Tournament Platform Successfully Deployed! ===
All abstract patterns working together harmoniously!""")
