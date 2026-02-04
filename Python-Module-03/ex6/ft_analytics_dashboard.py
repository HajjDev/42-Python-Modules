#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 14:51:22 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/04 17:43:13 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    events = {'players': {'alice': {'level': 41,
                                    'total_score': 2824,
                                    'sessions_played': 13,
                                    'favorite_mode': 'ranked',
                                    'achievements_count': 5},
                          'bob': {'level': 16,
                                  'total_score': 4657,
                                  'sessions_played': 27,
                                  'favorite_mode': 'ranked',
                                  'achievements_count': 2},
                          'charlie': {'level': 44,
                                      'total_score': 9935,
                                      'sessions_played': 21,
                                      'favorite_mode': 'ranked',
                                      'achievements_count': 7},
                          },
              'sessions': [{'player': 'bob',
                            'duration_minutes': 94,
                            'score': 1831,
                            'mode': 'competitive',
                            'completed': False},
                           {'player': 'bob',
                            'duration_minutes': 32,
                            'score': 1478,
                            'mode': 'casual',
                            'completed': True},
                           {'player': 'alice',
                            'duration_minutes': 98,
                            'score': 1981,
                            'mode': 'ranked',
                            'completed': True},
                           {'player': 'alice',
                            'duration_minutes': 53,
                            'score': 1238,
                            'mode': 'competitive',
                            'completed': False},
                           {'player': 'bob',
                            'duration_minutes': 52,
                            'score': 1555,
                            'mode': 'casual',
                            'completed': False},
                           {'player': 'charlie',
                            'duration_minutes': 56,
                            'score': 1196,
                            'mode': 'casual',
                            'completed': True},
                           {'player': 'charlie',
                            'duration_minutes': 22,
                            'score': 1110,
                            'mode': 'ranked',
                            'completed': False},
                           {'player': 'charlie',
                            'duration_minutes': 33,
                            'score': 666,
                            'mode': 'ranked',
                            'completed': False},
                           {'player': 'alice',
                            'duration_minutes': 101,
                            'score': 292,
                            'mode': 'casual',
                            'completed': True},
                           {'player': 'alice',
                            'duration_minutes': 42,
                            'score': 1880,
                            'mode': 'casual',
                            'completed': False},
                           {'player': 'alice',
                            'duration_minutes': 97,
                            'score': 1178,
                            'mode': 'ranked',
                            'completed': True},
                           {'player': 'bob',
                            'duration_minutes': 52,
                            'score': 761,
                            'mode': 'ranked',
                            'completed': True},
                           {'player': 'charlie',
                            'duration_minutes': 117,
                            'score': 1359,
                            'mode': 'casual',
                            'completed': True}],
              'game_modes': ['casual', 'competitive', 'ranked'],
              'achievements': ['first_blood', 'level_master', 'speed_runner',
                               'treasure_seeker', 'boss_hunter',
                               'pixel_perfect', 'combo_king', 'explorer']}
    print("=== List Comprehension Examples ===")
    high_scorers = [player for player in events['players'].keys()
                    if events["players"][player]["total_score"] > 2000]
    # high_scorers = []
    # for player in events['players'].keys():
    #    if events["players"][player]["total_score"] > 2000:
    #        high_scorers.append(player)

    scores_doubled = [events["players"][player]["total_score"] * 2
                      for player in events['players'].keys()]
    # scores_doubled = []
    # for player in events['players'].keys():
    #    scores_doubled.append(events["players"][player]["total_score"] * 2)

    active_players = list({session["player"]
                           for session in events['sessions']})
    # for session in events['sessions']:
    #    if session["player"] not in active_players:
    #        active_players.append(session["player"])

    print(f"High scorers (> 2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}\n")

    print("=== Dict Comprehension Examples ===")
    player_scores = {player: events["players"][player]["total_score"]
                     for player in events["players"]}
    # player_scores = {}
    # for player in events["players"]:
    #    player_scores[player] = events["players"][player]["total_score"]

    score_categories = {"high": 0, "medium": 0, "low": 0}
    for player in events["players"]:
        if events["players"][player]["total_score"] > 2000:
            score_categories["high"] += 1
        elif events["players"][player]["total_score"] > 1000:
            score_categories["medium"] += 1
        else:
            score_categories["low"] += 1

    ac = {player: events["players"][player]["achievements_count"]
          for player in events["players"]}
    # ac = {}
    # for player in events["players"]:
    #    ac[player] = events["players"][player]["achievements_count"]
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {ac}\n")

    print("=== Set Comprehension Examples ===")
    unique_players = {player for player in events["players"]}
    unique_achievements = {achievement
                           for achievement in events["achievements"]}
    modes = {mode for mode in events["game_modes"]}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Different Modes: {modes}\n")

    print("=== Combined Analysis ===")
    average = sum([player_scores[player]
                  for player in player_scores.keys()]) / len(unique_players)
    print(f"Total players: {len(unique_players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {average:.2f}")

    top_performer = ""
    current_top_score = 0
    for player in events["players"]:
        if events["players"][player]["total_score"] > current_top_score:
            current_top_score = events["players"][player]["total_score"]
            top_performer = player
    print(f"Top performer: {top_performer} \
({player_scores[top_performer]} points, {ac[top_performer]} achievements)")
