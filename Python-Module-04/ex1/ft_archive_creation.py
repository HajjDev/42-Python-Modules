#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/06 13:34:37 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/06 17:50:13 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main() -> None:
    """
    This function excutes the whole program.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")

    file = open("new_discovery.txt", "w")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    text = "[ENTRY 001] New quantum algorithm discovered\n[ENTRY 002] \
Efficiency increased by 347%\n[ENTRY 003] Archived by \
Data Archivist trainee\n"
    file.write(text)
    print(text)

    print("Data inscription complete. Storage unit sealed.")
    file.close()
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
