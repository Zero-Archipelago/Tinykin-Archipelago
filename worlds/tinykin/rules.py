from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule
from worlds.tinykin.TinyConstants import Area, Collectibles as Col

if TYPE_CHECKING:
    from worlds.tinykin import TinykinWorld

def set_all_rules(world: TinykinWorld) -> None:
    set_rules(world)
    set_completion_condition(world)

def get_rules(world: TinykinWorld):
    rules = {
        "entrances": {
        }
    }
    return rules

def set_rules(world: TinykinWorld) -> None:
    rules_lookup = get_rules(world)
    for entrance_name, rule in rules_lookup["entrances"].items():
        try:
            world.get_entrance(entrance_name).access_rule = rule
        except KeyError:
            pass

def set_completion_condition(world: TinykinWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.can_reach_location(f"Chrysal Workshop", world.player)