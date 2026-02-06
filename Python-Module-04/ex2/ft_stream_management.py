#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/06 13:43:40 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/06 17:55:46 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def main() -> None:
    """
    This function excutes the whole program.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    print("Input Stream active. Enter archivist ID: ", end="")
    sys.stdout.flush()
    archivist_id = sys.stdin.readline().strip()
    print("Input Stream active. Enter status report: ", end="")
    sys.stdout.flush()
    status_report = sys.stdin.readline().strip()
    print("")
    print(f"[STANDARD] Archive status from {archivist_id}: {status_report}")
    print("[ALERT] System diagnostic: Communication channels \
verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
