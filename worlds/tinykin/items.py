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

# Item Collectibles no Offset 0x0
KeyOffset: int = 0x100
LiftableOffset: int = 0x500
GrindsGlobalOffset: int = 0x1000
GrindsPerAreaOffset: int = 0x1200
GrindsSingleOffset: int = 0x1800
RopesGlobalOffset: int = 0x2000
RopesPerAreaOffset: int = 0x2200
RopesSingleOffset: int = 0x2800
TinykinGlobalOffset: int = 0x3000
TinykinPerAreaOffset: int = 0x4000
TinykinSingleOffset: int = 0x5000

item_table: Dict[str, ItemData] = {
    "Progressive Bubble": ItemData(id=0x1, amount=8),
    "Soapboard": ItemData(id=0x2),
    "Bouncing": ItemData(id=0x3),
    "Climbing": ItemData(id=0x4),
    "Cat Door Chip": ItemData(id=0x5),
    "Ticket": ItemData(id=0x6),

    "City of Sanctar Key": ItemData(id=KeyOffset + 0x0),
    "Lands of Ambrose Key": ItemData(id=KeyOffset + 0x1),

    "Transidor Crossing Flower Vase": ItemData(id=LiftableOffset + 0x0),

    "Grinding Rails": ItemData(id=GrindsGlobalOffset + 0x0),

    # "Chrysal Workshop - Grinding Rails": ItemData(id=GrindsGlobalOffset + 0x0),
    # "Transidor Crossing - Grinding Rails": ItemData(id=GrindsGlobalOffset + 0x1),
    # "City of Sanctar - Grinding Rails": ItemData(id=GrindsGlobalOffset + 0x2),
    # "Foliana Heights - Grinding Rails": ItemData(id=GrindsGlobalOffset + 0x3),
    # "Waters of Balnea - Grinding Rails": ItemData(id=GrindsGlobalOffset + 0x4),
    # "Lands of Ambrose - Grinding Rails": ItemData(id=GrindsGlobalOffset + 0x5),
    # "Cerelion Park - Grinding Rails": ItemData(id=GrindsGlobalOffset + 0x6),
    #
    # "City of Sanctar Grinding Chain - In front of cathedral to cat tree": ItemData(id=GrindsSingleOffset + 0x0),
    # "City of Sanctar Grinding Chain - Book shelve to cat tree": ItemData(id=GrindsSingleOffset + 0x1),
    # "City of Sanctar Grinding Chain - Piano to cat tree": ItemData(id=GrindsSingleOffset + 0x2),
    # "City of Sanctar Grinding Chain - Couch top to cat tree": ItemData(id=GrindsSingleOffset + 0x3),
    # "City of Sanctar Grinding Chain - Hifi shelve of cat tree": ItemData(id=GrindsSingleOffset + 0x4),
    # "Chrysal Workshop Grinding Chain - Ground to Transidor Crossing Vent": ItemData(id=GrindsSingleOffset + 0x5),
    # "Transidor Crossing Grinding Chain - Skateboard area to book tower": ItemData(id=GrindsSingleOffset + 0x6),
    # "Chrysal Workshop Grinding Chain - Transidor Crossing Vent to Museum": ItemData(id=GrindsSingleOffset + 0x7),
    # "Transidor Crossing Grinding Chain - Skateboad area to City of Sanctar door lock": ItemData(id=GrindsSingleOffset + 0x8),
    # "Foliana Heights Grinding Chain - Small plant to book pile under desk": ItemData(id=GrindsSingleOffset + 0x9),
    # "Foliana Heights Grinding Chain - Big plant to village": ItemData(id=GrindsSingleOffset + 0xA),
    # "Chrysal Workshop Grinding Chain - Waters of Balnea Vent to Celerion Park Vent": ItemData(id=GrindsSingleOffset + 0xB),
    # "Foliana Heights Grinding Chain - Big plant to terrarium top left": ItemData(id=GrindsSingleOffset + 0xC),
    # "Foliana Heights Grinding Chain - Big plant to small plant": ItemData(id=GrindsSingleOffset + 0xD),
    # "Foliana Heights Grinding Chain - Big plant to terrarium top right": ItemData(id=GrindsSingleOffset + 0xE),
    # "Foliana Heights Grinding Chain - Aquarium exit to big plant": ItemData(id=GrindsSingleOffset + 0xF),
    # "Foliana Heights Grinding Chain - High shelve to big plant": ItemData(id=GrindsSingleOffset + 0x10),
    # "Foliana Heights Grinding Chain - Top water spike area to top of big plant": ItemData(id=GrindsSingleOffset + 0x11),
    # "Foliana Heights Grinding Chain - Connection spike area": ItemData(id=GrindsSingleOffset + 0x12),
    # "Transidor Crossing Grinding Chain - Stairs bottom to top": ItemData(id=GrindsSingleOffset + 0x13),
    # "Transidor Crossing Grinding Chain - Stair railing to lower clock platform": ItemData(id=GrindsSingleOffset + 0x14),
    # "Transidor Crossing Grinding Chain - Celerion Park curtains to stair railing": ItemData(id=GrindsSingleOffset + 0x15),
    # "Transidor Crossing Grinding Chain - Upper shelve to stair railing": ItemData(id=GrindsSingleOffset + 0x16),

    "Ropes": ItemData(id=RopesGlobalOffset + 0x0),

    # "Chrysal Workshop - Ropes": ItemData(id=RopesPerAreaOffset + 0x0),
    # "Transidor Crossing - Ropes": ItemData(id=RopesPerAreaOffset + 0x1),
    # "City of Sanctar - Ropes": ItemData(id=RopesPerAreaOffset + 0x2),
    # "Foliana Heights - Ropes": ItemData(id=RopesPerAreaOffset + 0x3),
    # "Waters of Balnea - Ropes": ItemData(id=RopesPerAreaOffset + 0x4),
    # "Lands of Ambrose - Ropes": ItemData(id=RopesPerAreaOffset + 0x5),
    # "Cerelion Park - Ropes": ItemData(id=RopesPerAreaOffset + 0x6),

    # Ropes Single

    "Carrier Tinykin": ItemData(id=TinykinGlobalOffset + 0x0),
    "Explosive Tinykin": ItemData(id=TinykinGlobalOffset + 0x1),
    "Ladder Tinykin": ItemData(id=TinykinGlobalOffset + 0x2),
    "Electric Tinykin": ItemData(id=TinykinGlobalOffset + 0x3),
    "Bridge Tinykin": ItemData(id=TinykinGlobalOffset + 0x4),

    # "Transidor Crossing - Carrier Tinykins": ItemData(id=TinykinPerAreaOffset + 0x0),
    # "Transidor Crossing - Explosive Tinykins": ItemData(id=TinykinPerAreaOffset + 0x1),
    # "Transidor Crossing - Ladder Tinykins": ItemData(id=TinykinPerAreaOffset + 0x2),
    # "Transidor Crossing - Electric Tinykins": ItemData(id=TinykinPerAreaOffset + 0x3),
    # "Transidor Crossing - Bridge Tinykins": ItemData(id=TinykinPerAreaOffset + 0x4),
    # "City of Sanctar - Carrier Tinykins": ItemData(id=TinykinPerAreaOffset + 0x5),
    # "City of Sanctar - Explosive Tinykins": ItemData(id=TinykinPerAreaOffset + 0x6),
    # "City of Sanctar - Ladder Tinykins": ItemData(id=TinykinPerAreaOffset + 0x7),
    # "City of Sanctar - Electric Tinykins": ItemData(id=TinykinPerAreaOffset + 0x8),
    # "City of Sanctar - Bridge Tinykins": ItemData(id=TinykinPerAreaOffset + 0x9),
    # "Foliana Heights - Carrier Tinykins": ItemData(id=TinykinPerAreaOffset + 0xA),
    # "Foliana Heights - Explosive Tinykins": ItemData(id=TinykinPerAreaOffset + 0xB),
    # "Foliana Heights - Ladder Tinykins": ItemData(id=TinykinPerAreaOffset + 0xC),
    # "Foliana Heights - Electric Tinykins": ItemData(id=TinykinPerAreaOffset + 0xD),
    # "Foliana Heights - Bridge Tinykins": ItemData(id=TinykinPerAreaOffset + 0xE),
    # "Waters of Balnea - Carrier Tinykins": ItemData(id=TinykinPerAreaOffset + 0xF),
    # "Waters of Balnea - Explosive Tinykins": ItemData(id=TinykinPerAreaOffset + 0x10),
    # "Waters of Balnea - Ladder Tinykins": ItemData(id=TinykinPerAreaOffset + 0x11),
    # "Waters of Balnea - Electric Tinykins": ItemData(id=TinykinPerAreaOffset + 0x12),
    # "Waters of Balnea - Bridge Tinykins": ItemData(id=TinykinPerAreaOffset + 0x13),
    # "Lands of Ambrose - Carrier Tinykins": ItemData(id=TinykinPerAreaOffset + 0x14),
    # "Lands of Ambrose - Explosive Tinykins": ItemData(id=TinykinPerAreaOffset + 0x15),
    # "Lands of Ambrose - Ladder Tinykins": ItemData(id=TinykinPerAreaOffset + 0x16),
    # "Lands of Ambrose - Electric Tinykins": ItemData(id=TinykinPerAreaOffset + 0x17),
    # "Lands of Ambrose - Bridge Tinykins": ItemData(id=TinykinPerAreaOffset + 0x18),
    # "Cerelion Park - Carrier Tinykins": ItemData(id=TinykinPerAreaOffset + 0x19),
    # "Cerelion Park - Explosive Tinykins": ItemData(id=TinykinPerAreaOffset + 0x1A),
    # "Cerelion Park - Ladder Tinykins": ItemData(id=TinykinPerAreaOffset + 0x1B),
    # "Cerelion Park - Electric Tinykins": ItemData(id=TinykinPerAreaOffset + 0x1C),
    # "Cerelion Park - Bridge Tinykins": ItemData(id=TinykinPerAreaOffset + 0x1D),

    # "Transidor Crossing - Carrier Tinykin": ItemData(id=TinykinSingleOffset + 0x0, amount=0),
    # "Transidor Crossing - Explosive Tinykin": ItemData(id=TinykinSingleOffset + 0x1, amount=0),
    # "Transidor Crossing - Ladder Tinykin": ItemData(id=TinykinSingleOffset + 0x2, amount=0),
    # "Transidor Crossing - Electric Tinykin": ItemData(id=TinykinSingleOffset + 0x3, amount=0),
    # "Transidor Crossing - Bridge Tinykin": ItemData(id=TinykinSingleOffset + 0x4, amount=0),
    # "City of Sanctar - Carrier Tinykin": ItemData(id=TinykinSingleOffset + 0x5, amount=0),
    # "City of Sanctar - Explosive Tinykin": ItemData(id=TinykinSingleOffset + 0x6, amount=0),
    # "City of Sanctar - Ladder Tinykin": ItemData(id=TinykinSingleOffset + 0x7, amount=0),
    # "City of Sanctar - Electric Tinykin": ItemData(id=TinykinSingleOffset + 0x8, amount=0),
    # "City of Sanctar - Bridge Tinykin": ItemData(id=TinykinSingleOffset + 0x9, amount=0),
    # "Foliana Heights - Carrier Tinykin": ItemData(id=TinykinSingleOffset + 0xA, amount=0),
    # "Foliana Heights - Explosive Tinykin": ItemData(id=TinykinSingleOffset + 0xB, amount=0),
    # "Foliana Heights - Ladder Tinykin": ItemData(id=TinykinSingleOffset + 0xC, amount=0),
    # "Foliana Heights - Electric Tinykin": ItemData(id=TinykinSingleOffset + 0xD, amount=0),
    # "Foliana Heights - Bridge Tinykin": ItemData(id=TinykinSingleOffset + 0xE, amount=0),
    # "Waters of Balnea - Carrier Tinykin": ItemData(id=TinykinSingleOffset + 0xF, amount=0),
    # "Waters of Balnea - Explosive Tinykin": ItemData(id=TinykinSingleOffset + 0x10, amount=0),
    # "Waters of Balnea - Ladder Tinykin": ItemData(id=TinykinSingleOffset + 0x11, amount=0),
    # "Waters of Balnea - Electric Tinykin": ItemData(id=TinykinSingleOffset + 0x12, amount=0),
    # "Waters of Balnea - Bridge Tinykin": ItemData(id=TinykinSingleOffset + 0x13, amount=0),
    # "Lands of Ambrose - Carrier Tinykin": ItemData(id=TinykinSingleOffset + 0x14, amount=0),
    # "Lands of Ambrose - Explosive Tinykin": ItemData(id=TinykinSingleOffset + 0x15, amount=0),
    # "Lands of Ambrose - Ladder Tinykin": ItemData(id=TinykinSingleOffset + 0x16, amount=0),
    # "Lands of Ambrose - Electric Tinykin": ItemData(id=TinykinSingleOffset + 0x17, amount=0),
    # "Lands of Ambrose - Bridge Tinykin": ItemData(id=TinykinSingleOffset + 0x18, amount=0),
    # "Cerelion Park - Carrier Tinykin": ItemData(id=TinykinSingleOffset + 0x19, amount=0),
    # "Cerelion Park - Explosive Tinykin": ItemData(id=TinykinSingleOffset + 0x1A, amount=0),
    # "Cerelion Park - Ladder Tinykin": ItemData(id=TinykinSingleOffset + 0x1B, amount=0),
    # "Cerelion Park - Electric Tinykin": ItemData(id=TinykinSingleOffset + 0x1C, amount=0),
    # "Cerelion Park - Bridge Tinykin": ItemData(id=TinykinSingleOffset + 0x1D, amount=0),
    "Nothing": ItemData(id=0x999),
}

ITEM_NAME_TO_ID = {key: value.id for key, value in item_table.items()}


class TinykinItem(Item):
    game: str = "Tinykin"

def get_random_filler_item_name(world: TinykinWorld) -> str:
    filler_list = ["Nothing"]
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