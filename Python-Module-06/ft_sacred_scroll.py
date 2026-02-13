#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_sacred_scroll.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 10:27:13 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/13 16:38:48 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy
import alchemy.elements

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): \
{alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): \
{alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}\n")

    print("Testing package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")
    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")
