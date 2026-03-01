#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  higher_magic.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/26 07:51:12 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/27 13:48:44 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """
    This function combines two spells into one function.

    Args:
        spell1 (callable): The first spell.
        spell2 (callable): The second spell.

    Returns:
        callable: A function that is the combination of both.
    """
    return lambda *args: (spell1(*args), spell2(*args))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """
    This function amplifies a spell by multiplying the
    amount of power by a certain multiplier.

    Args:
        base_spell (callable): The spell to be amplified.
        multiplier (int): The multiplier.

    Returns:
        callable: A function that returns the amplified power
        of the spell.
    """
    return lambda *args: base_spell(*args) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    """
    This function casts a spell if a certain condition is fulfilled.

    Args:
        condition (callable): The condition to fulfill.
        spell (callable): The spell to be casted.

    Returns:
        callable: A function casting the spell if the condition is
        fulfilled, an error otherwise.
    """
    return lambda *args: spell(*args) if condition(*args) else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    """
    This function creates another function that
    applies each of the spells on specific arguments.

    Args:
        spells (list[callable]): The list of spells.

    Returns:
        callable: A function that applies it's arguments on the
        spells.
    """
    return lambda *args: list(map(lambda s: s(*args), spells))


if __name__ == "__main__":
    print("""=== Exercise 1 - Demo ===
Available Spells:
    - Spell1 with double power effect.
    - Spell2 with half power effect.
    - Spell 3 with no effect.\n""")
    spells = [lambda power: power * 2,
              lambda power: power // 2,
              lambda power: power
              ]
    print(f"""=== Spell Combiner ===
Combining Spell1 and Spell2.
Combined results with power = 4: {spell_combiner(spells[0], spells[1])(4)}
Combined results with power = 3: {spell_combiner(spells[0], spells[1])(2)}

=== Power Amplifier ===
Amplifying Spell1 and Spell2.
Spell1 before amplfifier and power = 2: {spells[0](2)}
Spell1 after amplfifier, power = 2 and multiplier = 3: \
{power_amplifier(spells[0], 3)(2)}

Spell2 before amplfifier and power = 1: {spells[1](1)}
Spell2 after amplfifier, power = 1 and multiplier = 2: \
{power_amplifier(spells[0], 2)(1)}

=== Conditional Caster ===
Testing conditional caster on Spell1 and Spell3, with condition power > 0.
Testing with Spell1 and power = -1: \
{conditional_caster(lambda x: x > 0, spells[0])(-1)}
Testing with Spell3 and power = 3: \
{conditional_caster(lambda x: x > 0, spells[2])(2)}

=== Spell Sequence ===
Testing sequence of spells with power = 2
Result: {spell_sequence(spells)(2)}""")
