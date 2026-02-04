#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/30 18:13:20 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/04 20:08:39 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    alice_achievements = set(['first_kill', 'level_10', 'treasure_hunter',
                              'speed_demon'])
    bob_achievements = set(['first_kill', 'level_10', 'boss_slayer',
                            'collector'])
    charlie_achievements = set(['level_10', 'treasure_hunter', 'boss_slayer',
                                'speed_demon', 'perfectionist'])
    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")

    print("\n=== Achievement Analytics ===")
    unique_achievements = alice_achievements.union(bob_achievements)
    unique_achievements = unique_achievements.union(charlie_achievements)
    print(f"All unique achivements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}\n")

    commn_achievements = alice_achievements.intersection(bob_achievements)
    commn_achievements = commn_achievements.intersection(charlie_achievements)
    print(f"Common to all players: {commn_achievements}")
    alice_unique = alice_achievements.difference(bob_achievements)
    alice_unique = alice_unique.difference(charlie_achievements)
    bob_unique = bob_achievements.difference(alice_achievements)
    bob_unique = bob_unique.difference(charlie_achievements)
    charlie_unique = charlie_achievements.difference(alice_achievements)
    charlie_unique = charlie_unique.difference(bob_achievements)
    print(f"Rare achievements (1 player): \
{alice_unique.union(bob_unique).union(charlie_unique)}\n")

    print(f"Alice vs BoB common: \
{alice_achievements.intersection(bob_achievements)}")
    print(f"Alice unique: {alice_achievements.difference(bob_achievements)}")
    print(f"Bob unique: {bob_achievements.difference(alice_achievements)}")
