#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/06 13:19:22 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/06 17:55:29 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main() -> None:
    """
    This function excutes the whole program.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        file = open("ancient_fragment.txt", "r")
        print(f"Accessing Storage Vault: {file.name}")
        content = file.read()
        print("Connection established...\n")

        print("RECOVERED DATA:")
        print(content)
        print("\nData recovery complete. Storage unit disconnected.")
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
