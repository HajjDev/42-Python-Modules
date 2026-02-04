#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/29 17:02:35 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 17:10:51 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# --- Package imports ---
import sys

# --- Tests and Main program ---
if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    number_of_scores = len(sys.argv)

    if number_of_scores < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py \
<score1> <score2> ...")
    else:
        try:
            scores: list[int] = []
            for score in sys.argv[1:]:
                scores.append(int(score))
            total_players = len(scores)
            total_score = sum(scores)
            average_score = total_score / total_players
            high_score = max(scores)
            low_score = min(scores)
            score_range = high_score - low_score
            print(f"""Scores processed: {scores}
Total players: {total_players}
Total score: {total_score}
Average score: {average_score}
High score: {high_score}
Low score: {low_score}
Score range: {score_range}
""")
        except ValueError:
            print("[ERROR]: Please make sure that all of the score are \
valid numbers.")
