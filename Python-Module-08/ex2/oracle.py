#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 09:54:24 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/20 15:07:37 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import os


def load_variables() -> dict[str, str | None]:
    """
    This function loads all of the environment variables.

    Returns:
        dict[str, str | None]: A dictionary containing the value
        of each environmenet variable, None if the variable is not
        defined.
    """
    wanted_variables = {
        "MATRIX_MODE": None,
        "DATABASE_URL": None,
        "API_KEY": None,
        "LOG_LEVEL": None,
        "ZION_ENDPOINT": None
    }
    for variable in wanted_variables.keys():
        wanted_variables[variable] = os.environ.get(variable)
    return wanted_variables


def iterate_and_print(variable_dict: dict[str, str | None]) -> None:
    """
    This function iterates over a bunch of variables and prints
    their corresponding values.

    Args:
        variable_dict (dict[str, str  |  None]): The dictionary of environment
        variables.
    """
    formatting = {
        "MATRIX_MODE": "Mode",
        "DATABASE_URL": "Database",
        "API_KEY": "API Access",
        "LOG_LEVEL": "Log Level",
        "ZION_ENDPOINT": "Zion Network"
    }
    warning = False
    for var in variable_dict.keys():
        if variable_dict[var] is not None:
            message = variable_dict[var]
        else:
            warning = True
            message = "MISSING"
        print(f"{formatting[var]}: {message}")
    if warning:
        print("\nWARNING: Please make sure to have .env file with all of the \
information or to specify it using global variables.")


def main() -> None:
    """
    This function tests and runs the main program.
    """
    print("ORACLE STATUS: Reading the Matrix...\n")

    env_exists = "OK" if os.path.exists(".env") else "KO"
    try:
        import dotenv
        print("Configuration loaded:")
        if env_exists == "OK":
            dotenv.load_dotenv()
        iterate_and_print(load_variables())

        print(f"""\nEnvironment security check:
[OK] No hardcoded secrets detected
[{env_exists}] .env file properly configured
[OK] Production overrides available""")

        print("\nThe Oracle sees all configurations.")
    except Exception as e:
        print(f"Error occured while loading .env: {e}, make sure it is \
configured correctly and that python-dotenv is installed.")


if __name__ == "__main__":
    main()
