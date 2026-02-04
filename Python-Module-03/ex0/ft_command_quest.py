#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/29 16:49:15 by cel-hajj        #+#    #+#               #
#  Updated: 2026/01/29 16:57:18 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# -- Package Imports ---
import sys

# --- Tests and Main program ---
if __name__ == "__main__":
    print("=== Command Quest ===")
    total_arguments = len(sys.argv)
    program_name = sys.argv[0]
    index = 1

    if total_arguments < 2:
        print(f"""No arguments provided!
Program name: {program_name}
Total arguments: {total_arguments}""")
    else:
        print(f"""Program name: {program_name}
Arguments received: {total_arguments - 1}""")
        while index < total_arguments:
            print(f"Argument {index}: {sys.argv[index]}")
            index += 1
        print(f"Total arguments: {total_arguments}")
