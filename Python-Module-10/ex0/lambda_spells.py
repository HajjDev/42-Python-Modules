#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 09:41:55 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/27 13:44:32 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    This function sorts a list of artifacts based on their
    powers.

    Args:
        artifacts (list[dict]): The artifacts list to sort.

    Returns:
        list[dict]: The sorted list.
    """
    return sorted(artifacts, key=lambda art: art["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """
    This functions filters a list of mages according to a
    minimum required power.

    Args:
        mages (list[dict]): The list of mages to filter.
        min_power (int): The minimum power.

    Returns:
        list[dict]: The filtered list of mages.
    """
    return list(filter(lambda mg: mg["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    This function transforms a list of spells into a new one
    by adding * on both sides of each spell.

    Args:
        spells (list[str]): The list of spells to be transformed.

    Returns:
        list[str]: The transformed list.
    """
    return list(map(lambda sp: "* " + sp + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """
    This function calculates the max, min and average of
    a list of mages.

    Args:
        mages (list[dict]): The list of mages.

    Returns:
        dict: A dictionary containing the statistics of the
        list of mages.
    """
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0}
    return {
        "max_power": max(map(lambda mg: mg["power"], mages)),
        "min_power": min(map(lambda mg: mg["power"], mages)),
        "avg_power": (round(sum(map(lambda mg: mg["power"], mages))
                            / len(mages), 2))
    }


if __name__ == "__main__":
    print("=== Exercise 0 - Demo ===\n")
    artifacts = [{'name': 'Crystal Orb', 'power': 96, 'type': 'weapon'},
                 {'name': 'Storm Crown', 'power': 102, 'type': 'relic'},
                 {'name': 'Lightning Rod', 'power': 67, 'type': 'focus'},
                 {'name': 'Shadow Blade', 'power': 107, 'type': 'relic'}]
    mages = [{'name': 'Ember', 'power': 88, 'element': 'earth'},
             {'name': 'Storm', 'power': 65, 'element': 'ice'},
             {'name': 'Sage', 'power': 80, 'element': 'water'},
             {'name': 'Riley', 'power': 100, 'element': 'light'},
             {'name': 'Ash', 'power': 57, 'element': 'ice'}]
    spells = ['earthquake', 'flash', 'blizzard', 'meteor']
    print(f"""=== Artifact Sorter ===
Before: {artifacts}

After: {artifact_sorter(artifacts)}


=== Power Filter ===
Before: {mages}

After: {power_filter(mages, 80)}


=== Spell Transformer ===
Before: {spells}

After: {spell_transformer(spells)}


=== Mage Stats ===
Mages: {mages}

Stats: {mage_stats(mages)}""")
