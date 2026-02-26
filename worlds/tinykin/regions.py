from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from worlds.tinykin import TinykinWorld

def create_and_connect_regions(world: TinykinWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: TinykinWorld) -> None:
    Test_Region = Region("1", world.player, world.multiworld)
    regions = [
        Test_Region,
    ]
    world.multiworld.regions += regions

def connect_regions(world: TinykinWorld) -> None:
    pass