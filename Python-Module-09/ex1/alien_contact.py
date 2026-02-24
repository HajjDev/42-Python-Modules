#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  alien_contact.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 13:51:21 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/24 20:31:56 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from datetime import datetime
from enum import Enum
from typing import Optional, Self
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(Enum):
    """
    This class represents an enumeration of different contact types used
    by the AlienContact model.
    """
    RADIO = 1
    VISUAL = 2
    PHYSICAL = 3
    TELEPATHIC = 4


class AlienContact(BaseModel):
    """
    A class representing a AlienContact model. A AlienContact can be
    initialized with an id, a timestamp, a location, a contact type, an signal
    strength duration minutes a witness count a message received
    and a verified status.
    """
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified:  bool = Field(default=False)

    @model_validator(mode='after')
    def validate_data(self) -> Self:
        """
        This function validates the data given to the object on creation.
        To be a valid model, an AlienContact must have an id that starts
        with 'AC', physical contact reports must be verified, elepathic contact
        requires at least 3 witnesses and strong signals (> 7.0) should include
        received messages.

        Raises:
            ValueError: In case the data is not valid.

        Returns:
            Self: An instance of the object it self.
        """
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' \
(Alien Contact)")
        elif (self.contact_type == ContactType.PHYSICAL
              and not self.is_verified):
            raise ValueError("Physical contact reports must be verified")
        elif (self.contact_type == ContactType.TELEPATHIC
              and self.witness_count < 3):
            raise ValueError("Telepathic contact requires at least 3 \
witnesses")
        elif self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include \
received messages")
        return self


def main() -> None:
    """
    Main program - runs the tests and the output.
    """
    print("""Alien Contact Log Validation
======================================""")
    valid_ac = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-02-24T20:00:00",
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True
    )
    print(f"""Valid contact report:
ID: {valid_ac.contact_id}
Type: {valid_ac.contact_type.name.lower()}
Location: {valid_ac.location}
Signal: {valid_ac.signal_strength}/10
Duration: {valid_ac.duration_minutes} minutes
Witnesses: {valid_ac.witness_count}
Message: {valid_ac.message_received}

======================================""")
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="2024_001",
            timestamp="2024-02-24T20:00:00",
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=8,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
    except ValidationError as e:
        print("Test - 1:", e.errors()[0]["msg"].split(', ')[1])
    try:
        unvalid_ac = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-02-24T20:00:00",
            location="Area 51, Nevada",
            contact_type=ContactType.PHYSICAL,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=3,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
        print(unvalid_ac)
    except ValidationError as e:
        print("Test - 2:", e.errors()[0]["msg"].split(', ')[1])
    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-02-24T20:00:00",
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
    except ValidationError as e:
        print("Test - 3:", e.errors()[0]["msg"].split(', ')[1])
    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-02-24T20:00:00",
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=7,
            message_received="",
            is_verified=True
        )
    except ValidationError as e:
        print("Test - 4:", e.errors()[0]["msg"].split(', ')[1])


if __name__ == "__main__":
    main()
