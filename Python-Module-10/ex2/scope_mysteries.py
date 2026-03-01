#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  scope_mysteries.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/26 19:11:10 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/27 14:03:51 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any


def mage_counter() -> callable:
    """
    This function creates a counter using closure to
    maintain the state of the couting variable.

    Returns:
        callable: A function serving as a counter.
    """
    counts = 0

    def counter() -> int:
        """
        This is the main counter function that adds 1 to the counter
        everytime it is called.

        Returns:
            int: The current count.
        """
        nonlocal counts
        counts += 1
        return counts
    return counter


def spell_accumulator(initial_power: int) -> callable:
    """
    This function creates an acumulator that accumulates power
    starting from initial power using closure.

    Args:
        initial_power (int): The initial power.

    Returns:
        callable: A function serving as the accumulator.
    """
    accumulated_power = initial_power

    def accumulator(power_to_add: int) -> int:
        """
        This functions represents the accumulator, any amount of power can be
        added using the accumulator.

        Args:
            power_to_add (int): The power to add.

        Returns:
            int: The total power accumulated.
        """
        nonlocal accumulated_power
        accumulated_power += power_to_add
        return accumulated_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    """
    This function creates a new function that shows the name
    and the enchatment type of a spell.

    Args:
        enchantment_type (str): The enchantment type of the spell.

    Returns:
        callable: The function that produces the information.
    """
    return lambda name: f"{enchantment_type} {name}"


def memory_vault() -> dict[str, callable]:
    """
    This function servers as a memory vault where we can
    store and recall values.

    Returns:
        dict[str, callable]: A dictionary containing the different operations
        and their corresponding functions.
    """
    memory = {}

    def store(key: Any, value: Any) -> None:
        """
        This function stores a key and a value in the memory.

        Args:
            key (Any): The key of the value.
            value (Any): The value to store.
        """
        memory[key] = value

    def recall(key: Any) -> Any:
        """
        This function recalls the value of a certain key in the memory.

        Args:
            key (Any): The key of the value to be recalled.

        Returns:
            Any: The value of the key if found, an error otherwise.
        """
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":
    print("=== Exercise 2 - Demo ===\n")

    counter = mage_counter()
    accumulator = spell_accumulator(10)
    enchantment = enchantment_factory("Flaming")
    vault = memory_vault()
    print(f"""=== Mage Counter ===
Call 1: {counter()}
Call 2: {counter()}
Call 3: {counter()}
...""")
    for i in range(26):
        counter()
    print(f"""Call 30: {counter()}

=== Spell Accumulator ===
Starting with initial power set to 10
Adding 4: {accumulator(4)}
Adding 20: {accumulator(20)}
Removing 8: {accumulator(-8)}

=== Enchantment Factory ===
Testing with 'sword' and 'katana' with enchatment type: Flaming.
'Sword' -> {enchantment("sword")}
'Katana' -> {enchantment("katana")}

=== Memory Vault ===
Adding pair (key='42', value='school')""")
    vault["store"]('42', 'school')
    print(f"""Looking up the value: {vault["recall"]('42')}

Trying with forbidden values: (key=41)
Result: {vault['recall']('41')}""")
