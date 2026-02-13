# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 10:36:06 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/13 16:40:23 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .elements import create_air, create_earth, create_fire, create_water


def healing_potion() -> str:
    return f"Healing potion brewed with {create_fire()} \
and {create_water()}"


def strength_potion() -> str:
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    return f"Invisibility potion brewed with {create_air()} and \
{create_water()}"


def wisdom_potion() -> str:
    return f"Wisdom potion brewed with all elements: {create_fire()} \
{create_water()} {create_earth()} {create_air()}"
