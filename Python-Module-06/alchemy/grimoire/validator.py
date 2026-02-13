# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  validator.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 08:14:09 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/13 16:44:39 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def validate_ingredients(ingredients: str) -> str:
    validation = ("fire" in ingredients or "water" in ingredients
                  or "earth" in ingredients or "air" in ingredients)
    if validation:
        validation = "VALID"
    else:
        validation = "INVALID"
    return f"{ingredients} - {validation}"
