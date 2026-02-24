#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  space_station.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 07:34:47 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/24 20:22:52 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    """
    A class representing a SpaceStation model. A SpaceStation can be
    initialized with an id, a name, a crew size, a power level, an oxygen level
    and a last maintenance time.
    It also has a operational status and optional notes.
    """
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    """
    Main program - runs the tests and the output.
    """
    print("""Space Station Data Validation
========================================""")
    space_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2024-02-24T10:30:00",
        is_operational=True,
        notes=None
    )
    print(f"""Validation station created:
ID: {space_station.station_id}
Name: {space_station.name}
Crew: {space_station.crew_size} people
Power: {space_station.power_level}%
Oxygen: {space_station.oxygen_level}%
Status: {"Operational" if space_station.is_operational else "Not Operational"}

========================================""")
    print("Expected validation error")
    try:
        space_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            is_operational=True,
            notes=None
        )
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
