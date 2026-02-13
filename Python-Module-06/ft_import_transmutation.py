#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_import_transmutation.py                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 10:35:55 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/13 16:45:37 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.elements

from alchemy.elements import create_water

from alchemy.potions import healing_potion as heal

from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion


if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): \
{alchemy.elements.create_fire()}\n")

    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}\n")

    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}\n")

    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}\n")

    print("All import transmutation methods mastered!")
