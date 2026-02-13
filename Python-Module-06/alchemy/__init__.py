# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __init__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/12 10:25:42 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/12 10:34:51 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

__version__ = "1.0.0"
__author__ = "Master Pythonicus"

from .elements import create_fire, create_water

__all__ = ["create_fire", "create_water"]
