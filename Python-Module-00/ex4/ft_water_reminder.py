# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 13:44:38 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/28 13:44:42 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_water_reminder() -> None:
    number_of_days = int(input("Days since last watering: "))
    if (number_of_days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
