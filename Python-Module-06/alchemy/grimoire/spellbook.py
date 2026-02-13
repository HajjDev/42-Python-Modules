# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  spellbook.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 08:44:10 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/13 16:44:33 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)
    if "INVALID" in validation_result:
        status = "rejected"
    else:
        status = "recorded"
    return f"Spell {status}: {spell_name} ({validation_result})"
