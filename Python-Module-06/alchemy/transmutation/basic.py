# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  basic.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 07:47:01 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/13 16:41:48 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    return f"Stone transmuted to gem using {create_earth()}"
