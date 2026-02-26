from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification as IC, Location
from worlds.tinykin import items

if TYPE_CHECKING:
    from worlds.tinykin import TinykinWorld

LOCATION_NAME_TO_ID = {
    "Starting Bubble": 11,
    "Bubble Upgrade 1": 12,
    "Bubble Upgrade 2": 13,
    "Bubble Upgrade 3": 14,
    "Bubble Upgrade 4": 15,
    "Bubble Upgrade 5": 16,
    "Bubble Upgrade 6": 17,
    "Bubble Upgrade 7": 18,
    "Starting Soapboard": 2,
}

class TinykinLocation(Location):
    game: str = "Tinykin"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: TinykinWorld) -> None:
    create_regular_locations(world)

def create_regular_locations(world: TinykinWorld) -> None:
    Test_Region = world.get_region("1")
    Test_Location = get_location_names_with_ids(
        [
            "Starting Bubble",
            "Bubble Upgrade 1",
            "Bubble Upgrade 2",
            "Bubble Upgrade 3",
            "Bubble Upgrade 4",
            "Bubble Upgrade 5",
            "Bubble Upgrade 6",
            "Bubble Upgrade 7",
            "Starting Soapboard",
        ]
    )
    Test_Region.add_locations(Test_Location, TinykinLocation)