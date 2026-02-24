#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  space_crew.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 07:49:31 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/24 20:33:46 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from datetime import datetime
from enum import Enum
from typing import Self
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(Enum):
    """
    This class represents an enumeration of different ranks given to
    crew members.
    """
    CADET = 1
    OFFICER = 2
    LIEUTENANT = 3
    CAPTAIN = 4
    COMMANDER = 5


class CrewMember(BaseModel):
    """
    A class representing a CrewMember model. A CrewMember can be
    initialized with an id, a name, a rank, an age, a specialization
    years of experience and an active status.
    """
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """
    A class representing a SpaceMission model. A SpaceMission can be
    initialized with an id, a name, a destination, a launch_date, a duration
    a crew, a mission status and a budget.
    """
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_data(self) -> Self:
        """
        This function validates the data given to the object on creation.
        To be a valid model, a SpaceMission must have an ID that starts
        with 'M', have at least one Commander or Captain, long missions
        (> 365 days) need 50% experienced crew (5+ years) and all crew
        members must be active.

        Raises:
            ValueError: In case the data is not valid.

        Returns:
            Self: An instance of the object it self.
        """
        half = len(self.crew) / 2
        validation_requirements = {
            "starts_with_M": self.mission_id.startswith("M"),
            "commander_or_captain": any(member.rank == Rank.COMMANDER
                                        or member.rank == Rank.CAPTAIN
                                        for member in self.crew),
            "lm_requirements": sum([1 for member in self.crew
                                    if member.years_experience >= 5]) >= half,
            "all_active": all(member.is_active for member in self.crew)
        }
        if not validation_requirements["starts_with_M"]:
            raise ValueError('Mission ID must start with "M"')
        elif not validation_requirements["commander_or_captain"]:
            raise ValueError('Must have at least one Commander or Captain')
        elif (self.duration_days > 365
              and not validation_requirements["lm_requirements"]):
            raise ValueError("Long missions (> 365 days) need 50% experienced \
crew (5+ years)")
        elif not validation_requirements["all_active"]:
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    """
    Main program - runs the tests and the output.
    """
    print("""Space Mission Crew Validation
=========================================""")
    s_m = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-02-24T20:00:00",
        duration_days=900,
        crew=[CrewMember(
            member_id="M01",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=52,
            specialization="Mission Command",
            years_experience=6,
            is_active=True
                ),
              CrewMember(
            member_id="M02",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=32,
            specialization="Navigation",
            years_experience=6,
            is_active=True
                ),
              CrewMember(
            member_id="M03",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=45,
            specialization="Engineering",
            years_experience=8,
            is_active=True
                ),
              CrewMember(
            member_id="M04",
            name="Charbel El Hajj",
            rank=Rank.CADET,
            age=28,
            specialization="Control",
            years_experience=2,
            is_active=True
                )
              ],
        budget_millions=2500.0
    )
    print(f"""Valid mission created:
Mission: {s_m.mission_name}
ID: {s_m.mission_id}
Destination: {s_m.destination}
Duration: {s_m.duration_days} days
Budget: ${s_m.budget_millions}M
Crew size: {len(s_m.crew)}
Crew members:""")
    for i in range(len(s_m.crew)):
        print(f"- {s_m.crew[i].name} ({s_m.crew[i].rank.name.lower()}) \
- {s_m.crew[i].specialization}")
    print("\n=========================================")

    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-02-24T20:00:00",
            duration_days=900,
            crew=[CrewMember(
                member_id="M01",
                name="Sarah Connor",
                rank=Rank.LIEUTENANT,
                age=52,
                specialization="Mission Command",
                years_experience=6,
                is_active=True
                )],
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(f"Test - 1: {e.errors()[0]['msg'].split(', ')[1]}")
    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-02-24T20:00:00",
            duration_days=900,
            crew=[CrewMember(
                member_id="M01",
                name="Sarah Connor",
                rank=Rank.LIEUTENANT,
                age=52,
                specialization="Mission Command",
                years_experience=6,
                is_active=True
                ),
                CrewMember(
                member_id="M02",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=32,
                specialization="Navigation",
                years_experience=6,
                is_active=True
                ),
                CrewMember(
                member_id="M03",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=45,
                specialization="Engineering",
                years_experience=8,
                is_active=True
                ),
                CrewMember(
                member_id="M04",
                name="Charbel El Hajj",
                rank=Rank.CADET,
                age=28,
                specialization="Control",
                years_experience=2,
                is_active=True
                )
                  ],
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(f"Test - 2: {e.errors()[0]['msg'].split(', ')[1]}")
    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-02-24T20:00:00",
            duration_days=900,
            crew=[CrewMember(
                member_id="M01",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=52,
                specialization="Mission Command",
                years_experience=6,
                is_active=True
                ),
                CrewMember(
                member_id="M02",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=32,
                specialization="Navigation",
                years_experience=2,
                is_active=True
                ),
                CrewMember(
                member_id="M03",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=45,
                specialization="Engineering",
                years_experience=2,
                is_active=True
                ),
                CrewMember(
                member_id="M04",
                name="Charbel El Hajj",
                rank=Rank.CADET,
                age=28,
                specialization="Control",
                years_experience=2,
                is_active=True
                )
                  ],
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(f"Test - 3: {e.errors()[0]['msg'].split(', ')[1]}")
    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-02-24T20:00:00",
            duration_days=900,
            crew=[CrewMember(
                member_id="M01",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=52,
                specialization="Mission Command",
                years_experience=6,
                is_active=True
                ),
                CrewMember(
                member_id="M02",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=32,
                specialization="Navigation",
                years_experience=6,
                is_active=True
                ),
                CrewMember(
                member_id="M03",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=45,
                specialization="Engineering",
                years_experience=8,
                is_active=True
                ),
                CrewMember(
                member_id="M04",
                name="Charbel El Hajj",
                rank=Rank.CADET,
                age=28,
                specialization="Control",
                years_experience=2,
                is_active=False
                )
                  ],
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(f"Test - 4: {e.errors()[0]['msg'].split(', ')[1]}")


if __name__ == "__main__":
    main()
