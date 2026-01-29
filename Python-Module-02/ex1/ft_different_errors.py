#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/29 13:55:41 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 17:43:54 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def garden_operations() -> None:
    """
    This function simulates garden operations that trigger different errors.
    It is used to demonstrate catching multiple errors at once.
    """
    print("Testing multiple errors together...")
    # These operations are simulations. The first one will raise an error
    # and stop the function execution, which is expected behavior for this
    # demo.
    int("abc")
    division_by_zero = 1 / 0
    print(division_by_zero)
    missing_file = open("missing_file.txt")
    missing_file.close()
    prop_dict: dict[str, int] = {}
    print(prop_dict["missing_plant"])


def test_error_types() -> None:
    """
    Tests each error type individually and then tests catching multiple
    errors using garden_operations.
    """
    # ValueError
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    # ZeroDivisionError
    try:
        print("Testing ZeroDivisionError...")
        result = 1 / 0
        print(result)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    # FileNotFoundError
    try:
        print("Testing FileNotFoundError...")
        missing_file = open("missing_file.txt")
        missing_file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    # KeyError
    try:
        print("Testing KeyError...")
        prop_dict: dict[str, int] = {}
        print(prop_dict["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")

    # Multiple Errors Together
    try:
        garden_operations()
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


# --- Tests and Main program ---
if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("\nAll error types tested successfully!")
