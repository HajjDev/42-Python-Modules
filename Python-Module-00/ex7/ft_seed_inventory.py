# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 13:44:59 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/28 13:45:02 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit != "packets" and unit != "area" and unit != "grams":
        print("Unknown unit type")
    else:
        seed_type = seed_type.capitalize()
        if unit == "packets":
            print(f"{seed_type} seeds: {quantity} {unit} available")
        elif unit == "grams":
            print(f"{seed_type} seeds: {quantity} {unit} total")
        else:
            print(f"{seed_type} seeds: covers {quantity} square meters")
