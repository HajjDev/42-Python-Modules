# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_summary.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 13:44:54 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/28 13:44:57 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_garden_summary() -> None:
    garden_name = input("Enter garden name: ")
    plants_number = input("Enter number of plants: ")

    print(f"Garden: {garden_name}")
    print(f"Plants: {plants_number}")
    print("Status: Growing well!")
