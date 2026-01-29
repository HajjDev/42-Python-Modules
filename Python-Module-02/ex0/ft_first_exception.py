#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/29 13:40:49 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 17:43:11 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_temperature(temp_str: str) -> str:
    """
    This function checks if a given temperature is suitable for plants.
    Displays an error if the temperature is not valid. A valid temperature
    is a temperature T such that: 0 <= T <= 40

    Args:
        temp_str (str): The temperature to be checked

    Returns:
        str: The temperature if the temperature is valid, an empty string
        otherwise
    """
    print(f"Testing temperature: {temp_str}")
    try:
        int_temperature = int(temp_str)
        if (0 <= int_temperature <= 40):
            print(f"Temperature {int_temperature}°C is perfect for plants!")
            return temp_str
        else:
            if (int_temperature < 0):
                print(f"Error: {int_temperature}°C is too cold for plants "
                      "(min 0°C)")
            else:
                print(f"Error: {int_temperature}°C is too hot for plants "
                      "(max 40°C)")
            return ""
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return ""


def test_temperature_input() -> None:
    """
    Demonstrates the functionality of check_temperature with various inputs.
    """
    check_temperature("25")
    print("")
    check_temperature('abc')
    print("")
    check_temperature("100")
    print("")
    check_temperature("-50")


# --- Tests and Main program ---
if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
    print("\nAll tests completed - program didn't crash!")
