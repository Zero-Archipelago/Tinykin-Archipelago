from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification as IC, Location
from worlds.tinykin import items
from worlds.tinykin.TinyConstants import Area, Collectibles as Col, Tinykin
from worlds.tinykin.GameData.TinykinEggs import TinykinEggs


if TYPE_CHECKING:
    from worlds.tinykin import TinykinWorld

HubOffset: int = 0x10000
HallOffset: int = 0x20000
SanctarOffset: int = 0x30000
FolianaOffset: int = 0x40000
BalneaOffset: int = 0x50000
AmbroseOffset: int = 0x60000
ParkOffset: int = 0x70000
AtticOffset: int = 0x80000

TinykinEggOffset: int = 0x1000

TinykinCarrierOffset: int = 0x0
TinykinExplosiveOffset: int = 0x200
TinykinLadderOffset: int = 0x400
TinykinElectricOffset: int = 0x600
TinykinBridgeOffset: int = 0x800


LOCATION_NAME_TO_ID = {
    "Chrysal Workshop": 1,
    **{
        f"{area} {tinykin_type} Egg {egg_id}": location_id
        for location_id, (area, tinykin_type, egg_id) in TinykinEggs.items()
    }
}

class TinykinLocation(Location):
    game: str = "Tinykin"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: TinykinWorld) -> None:
    create_regular_locations(world)

def create_regular_locations(world: TinykinWorld) -> None:
    Workshop = world.get_region("Chrysal Workshop")

    Locations = get_location_names_with_ids(
        [
            *[location for location, ID in LOCATION_NAME_TO_ID.items()],

            "Chrysal Workshop",
        ]
    )

    Workshop.add_locations(Locations, TinykinLocation)