#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_pathway_debate.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 07:46:55 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/13 08:03:42 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
import alchemy

if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}\n")

    print("Testing Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}\n")

    print("Testing Package Access:")
    print(f"alchemy.transmutation.lead_to_gold(): \
{alchemy.transmutation.lead_to_gold()}")
    print(f"alchemy.transmutation.philosophers_stone(): \
{alchemy.transmutation.philosophers_stone()}\n")

    print("Both pathways work! Absolute: clear, Relative: concise")
