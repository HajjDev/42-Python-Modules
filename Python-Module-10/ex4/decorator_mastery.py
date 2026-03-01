#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  decorator_mastery.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/27 08:37:18 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/27 14:33:34 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import functools
import datetime
from typing import Any


def spell_timer(func: callable) -> callable:
    """
    This function servers as the main decorator. This decorator
    calculates the time taken by a function to execute.

    Args:
        func (callable): The function to execute and calculate execution
        time.

    Returns:
        callable: A new function that calculates the time.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """
        This is the main wrapper of the decorator that executes the
        function and prints the time taken.

        Returns:
            Any: The result of te function.
        """
        print(f"Casting {func.__name__}...")
        current_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        elapsed_time = (datetime.datetime.now() - current_time).total_seconds()
        print(f"Spell completed in {elapsed_time:.6f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    """
    This function wraps the main decorator. This function
    validates the power of a spell based on a threshold of power.

    Args:
        min_power (int): The power threshold.

    Returns:
        callable: A new function that does the validation.
    """
    def decorator(func: callable) -> callable:
        """
        This function is an arbitrary function that serves as the decorator
        that will take the spell and execute the validation.

        Args:
            func (callable): The spell to be validated.

        Raises:
            ValueError: If the arguments of the spell are not valid.

        Returns:
            callable: The function that calculates the difference.
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            """
            This is the main wrapper of the decorator that executes what's
            needed.

            Raises:
                ValueError: If the arguments of the spell are not valid.

            Returns:
                Any: The result of the function if the function is valid,
                an error otherwise.
            """
            if "power" in kwargs and isinstance(kwargs["power"], int):
                power = kwargs["power"]
            elif len(args) > 2 and isinstance(args[2], int):
                power = args[2]
            elif len(args) > 0 and isinstance(args[0], int):
                power = args[0]
            else:
                raise ValueError("Please provide valid arguments to the \
function.")
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    """
    This function retries to cast a spell if the cast
    failed. A cast fails if the spell doesn't have enough
    power.

    Args:
        max_attempts (int): The maximum attempts allowed.

    Returns:
        callable: A function that retries to cast the spell max_attempts
        times.
    """
    def decorator(func: callable) -> callable:
        """
        This is the main decorator of the wrapper that will take
        the function and call the wrapper to retry the execution.

        Args:
            func (callable): The spell to be casted.

        Returns:
            callable: The function that retries the execution.
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            """
            This function is the wrapper that executes the retry
            of the funtion max_attempts times.

            Returns:
                Any: The result of the function if succesful, an error
                oterhwise.
            """
            for i in range(1, max_attempts + 1):
                result = func(*args, **kwargs)
                if result == "Insufficient power for this spell":
                    print(f"Spell failed, retrying... \
(attempt {i}/{max_attempts})")
                else:
                    return result
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """
    This class represents a guild of mages that can cast spells.
    """
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        This function validates the name given to the guild. A name
        is valid if it contains more than 3 characters and consist of only
        letters and spaces.

        Args:
            name (str): The name of the guild.

        Returns:
            bool: True if the name is valid, false otherwise.
        """
        return len(name) >= 3 and all(char.isspace() or char.isalpha()
                                      for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """
        """
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("=== Exercise 4 - Demo ===\n")
    spells = [("Fireball", 13), ("SnowBall", 7), ("Lightning", 12)]
    guild = MageGuild()

    print(f"""=== Validate Mage Name ===
Testing valid name: 'Hello, bonjour'
Result: {MageGuild.validate_mage_name('Hello bonjour')}

Testing invalid name: 'Hello 42'
Result: {MageGuild.validate_mage_name('Hello 42')}

Testing valid name: '   jiji azd a   '
Result: {MageGuild.validate_mage_name('   jiji azd a   ')}\n""")

    @spell_timer
    def spells_time(spell: tuple) -> str:
        guild = MageGuild()
        try:
            return guild.cast_spell(spell[0], spell[1])
        except Exception as e:
            return e

    @retry_spell(max_attempts=10)
    def spells_retry(spell: tuple) -> str:
        guild = MageGuild()
        return guild.cast_spell(spell[0], spell[1])

    print(f"""=== Spell Timer ===
Testing Spell timer with spells: {spells}\n""")
    for spell in spells:
        result = spells_time(spell)
        print(f"{spell[0]}: {result}\n")

    print(f"""=== Power Validator ===
Testing power validator with spells: {spells} and no valid arguments.\n""")
    for spell in spells:
        try:
            print(f"{spell[0]}: {guild.cast_spell(spell[0], spell[1])}")
        except Exception as e:
            print(f"{spell[0]}: {e}")
    try:
        guild.cast_spell("a", "p")
    except Exception as e:
        print("No valid arguments:", e)

    print(f"""\n=== Retry Spell ===
Testing retry spell on spells: {spells}\n""")
    for i in range(len(spells)):
        print(f"{spells[i]}: {spells_retry(spells[i])}" + ('\n'
              if i < len(spells) - 1 else ""))
