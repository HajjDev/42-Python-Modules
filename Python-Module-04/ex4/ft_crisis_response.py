#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_crisis_response.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/06 18:04:16 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/06 18:27:12 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main() -> None:
    """
    This function excutes the whole program.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    try:
        print("CRISIS ALERT: Attempting access to \
'classified_vault.txt'...")
        with open("classified_vault.txt", "r") as file:
            content = file.read()
            print(content)
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except FileNotFoundError:
        print("RESPONSE: Vault not found")
        print("STATUS: Crisis handled\n")

    try:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt", "r") as file:
            content = file.read()
            print(f'SUCCESS: Archive recovered - "{content}"')
            print("STATUS: Normal operations resumed\n")
    except Exception as e:
        print(f"RESPONSE: {e}")
        print("STATUS: Crisis handled, routine maintained\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
