# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 13:44:45 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/28 13:44:47 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_iterative() -> None:
    days_until_harvest = int(input("Days until harvest: "))

    for i in range(1, days_until_harvest + 1):
        print(f"Day {i}")
    print("Harvest time!")
