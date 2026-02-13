# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  advanced.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 07:47:15 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/13 16:42:02 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    return f"Philosopher’s stone created using {lead_to_gold()} \
and {healing_potion()}"


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
