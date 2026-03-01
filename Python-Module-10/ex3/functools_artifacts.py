#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  functools_artifacts.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/27 07:45:10 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/27 14:14:02 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import functools
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    This function reduces a list of spell powers by either calculating
    the sum, the product, the max or the min of the list.

    Args:
        spells (list[int]): The list of spell powers.
        operation (str): The operation to be executed.

    Returns:
        int: The result of the operation.
    """
    if operation not in ["add", "multiply", "max", "min"]:
        return -1
    else:
        if operation == "add":
            return functools.reduce(operator.add, spells)
        elif operation == "multiply":
            return functools.reduce(operator.mul, spells)
        elif operation == "max":
            return functools.reduce(max, spells)
        else:
            return functools.reduce(min, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """
    This function creates partial functions based on a function that
    have different attributes.

    Args:
        base_enchantment (callable): The base enchantemnt.

    Returns:
        dict[str, callable]: A dictionary containing the different partial
        functions and their names.
    """
    return {
        "fire_enchant": functools.partial(base_enchantment,
                                          power=50, element="fire"),
        "ice_enchant": functools.partial(base_enchantment,
                                         power=50, element="ice"),
        "lightning_enchant": functools.partial(base_enchantment,
                                               power=50, element="lightning")
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    """
    This function calculates the nth number of the
    fibonacci sequence using the lru cache to make the operations
    faster.

    Args:
        n (int): The position of the number wanted.

    Returns:
        int: The nth number of the fibonacci sequence.
    """
    if n < 0:
        print("Please make sure to only input  positive numbers!")
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """
    This function creates a dispatcher that behaves differently on
    the types of data given.

    Returns:
        callable: A function that behaves differently according to
        the arguments given to it.
    """
    @functools.singledispatch
    def spell(spells: Any) -> str:
        """
        This function serves as the main dispatcher that can take any type
        of data.

        Args:
            spells (Any): The spell given.

        Returns:
            str: Information on the execution of the spell.
        """
        return """Spell has been called with a non-supported argument
Spell: Regular Spell
Speciality: None"""

    @spell.register(int)
    def _1(spells: int) -> str:
        """
        This function serves as the int variant of the spell that can take a
        int representing damage.

        Args:
            spells (int): The damage given.

        Returns:
            str: Information on the execution of the spell.
        """
        return f"""Spell has been called with an int argument
Spell: Damage Spell
Speciality: {spells} damage"""

    @spell.register(str)
    def _2(spells: str) -> str:
        """
        This function serves as the str variant of the spell that can take a
        str representing an enchantment.

        Args:
            spells (str): The enchatment given.

        Returns:
            str: Information on the execution of the spell.
        """
        return f"""Spell has been called with a str argument
Spell: Enchantment Spell
Speciality: {spells} enchantment"""

    @spell.register(list)
    def _3(spells: list) -> str:
        """
        This function serves as the list variant of the spell that can take a
        list and executes each spell.

        Args:
            spells (list): The list of spells.

        Returns:
            str: Information on all of the executions of the spells.
        """
        msg = """Spell has been called with a list argument
Initializing multi-cast...\n"""
        for s in spells:
            msg += f"\n{spell(s)}\n"
        return msg

    return spell


if __name__ == "__main__":
    print("=== Exercise 3 - Demo ===\n")

    def base_enchantment(power: int, element: str, target: str):
        return f"Attacked {target} with {element} enchant using {power} power!"

    enchanter = partial_enchanter(base_enchantment)
    dispatcher = spell_dispatcher()
    spell_powers = [30, 11, 21, 13, 27, 19]
    fib_values = [0, 1, 5, 10, 1, 5, 20, 40]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [10, 14, 9]
    print(f"""=== Spell Reducer ===
Reducing Spells {spell_powers}\n""")
    for op in operations:
        print(f"Operation {op}:", spell_reducer(spell_powers, op))
    print(f"""\nTesting invalid operation: 'div'
Result: {spell_reducer(spell_powers, 'div')}

=== Partial Enchanter ===
Testing different echants with target = 'monster',\n""")
    for ench in ["fire_enchant", "ice_enchant", "lightning_enchant"]:
        print(f"Testing {ench}: {enchanter[f'{ench}'](target='monster')}")

    print(f"""\n=== Memoized fibonacci ===
Testing memoized fibonacci with values {fib_values}.\n""")
    for val in fib_values:
        print(f"fib({val}): {memoized_fibonacci(val)}")

    print(f"""\n=== Spell Dispatcher ===

Testing with no specified type: 'float'
{dispatcher(3.0)}

Testing with specified type: 'int'
{dispatcher(8)}

Testing with specified type: 'str'
{dispatcher("Ice")}

Testing with specified type: 'list'
{dispatcher([(0, 9), 10, "Fire"])}""")
