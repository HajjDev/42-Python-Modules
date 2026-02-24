#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  construct.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 18:53:38 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/20 14:56:38 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import os
import site


def main() -> None:
    """
    This function tests and runs the main program.
    """
    try:
        # This variable checks whether the code is executed
        # inside a virtual environment or not.
        in_environment = sys.prefix != sys.base_prefix
        if in_environment:
            print("MATRIX STATUS: Welcome to the construct\n")

            print(f"""Current Python: {sys.executable}
Virtual Environment: {os.path.basename(sys.prefix)}
Environment Path: {sys.prefix}\n""")

            print("""SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.\n""")

            print("Package installation path:")
            print(site.getusersitepackages())
        else:
            print("MATRIX STATUS: You're still plugged in\n")

            print(f"""Current Python: {sys.executable}
Virtual Environment: None detected\n""")

            print("""WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env\\Scripts\\activate    # On Windows

Then run this program again.""")
    except Exception as e:
        print(f"An error occured in the matrix: {e}")


if __name__ == "__main__":
    main()
