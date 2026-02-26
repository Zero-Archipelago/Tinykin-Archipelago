from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict
from BaseClasses import Item, ItemClassification as IC
import random

if TYPE_CHECKING:
    from worlds.tinykin import TinykinWorld


@dataclass
class ItemData:
    id: int
    classification: IC = IC.progression
    amount: int = 1


item_table: Dict[str, ItemData] = {
    "Progressive Bubble": ItemData(id=1, amount=8),
    "Soapboard": ItemData(id=2),
}

ITEM_NAME_TO_ID = {key: value.id for key, value in item_table.items()}


class TinykinItem(Item):
    game: str = "Tinykin"

def get_random_filler_item_name(world: TinykinWorld) -> str:
    filler_list = ["Test Filler"]
    return filler_list[0]

def create_item_with_correct_classification(world: TinykinWorld, name: str) -> TinykinItem:
    classification = item_table[name].classification
    id = item_table[name].id

    return TinykinItem(name, classification, id, world.player)

def create_all_items(world: TinykinWorld) -> None:
    item_pool: list[TinykinItem] = []
    for item in item_table:
        for _ in range(item_table[item].amount):
            item_pool.append(world.create_item(item))

    number_of_items = len(item_pool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += item_pool