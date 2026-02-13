# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_circular_curse.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 08:13:35 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/13 09:09:24 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.grimoire import validate_ingredients, record_spell

if __name__ == "__main__":
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print(f'validate_ingredients("fire air"): \
{validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): \
{validate_ingredients("dragon scales")}\n')

    print("Testing spell recording with validation:")
    print(f'record_spell("Fireball", "fire air"): \
{record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): \
{record_spell("Dark Magic", "shadow")}\n')

    print("Testing late import technique:")
    print(f'record_spell("Lightning", "air"): \
{record_spell("Lightning", "air")}\n')

    print("""Circular dependency curse avoided using late imports!
All spells processed safely!""")
