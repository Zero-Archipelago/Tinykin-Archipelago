from worlds.AutoWorld import World
from typing import Mapping, Any

from worlds.tinykin import items, regions, locations, rules, web_world, options

class TinykinWorld(World):
    """
    Tinykin is a colorful puzzle platformer where you explore a giant house as a tiny astronaut,
    using adorable creatures to solve environmental challenges. It blends light platforming,
    clever physics-based puzzles, and cozy exploration into a relaxing, surprisingly thoughtful adventure.
    """

    game: str = "Tinykin"

    web = web_world.TinykinWebWorld()

    options_dataclass = options.TinykinOptions
    options: options.TinykinOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Chrysal Workshop"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.TinykinItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {}
        #return slot_data