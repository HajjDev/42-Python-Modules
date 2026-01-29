# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 13:44:49 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/28 13:44:53 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_helper_recursive(days_until_harvest: int) -> None:
    if days_until_harvest == 0:
        return
    ft_helper_recursive(days_until_harvest - 1)
    print(f"Day {days_until_harvest}")


def ft_count_harvest_recursive() -> None:
    days_until_harvest = int(input("Days until harvest: "))
    ft_helper_recursive(days_until_harvest)
    print("Harvest time!")
