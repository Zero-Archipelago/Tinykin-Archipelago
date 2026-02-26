from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld
from worlds.tinykin.options import option_groups, option_presets

class TinykinWebWorld(WebWorld):
    game: str = "Tinykin"
    theme = "partyTime"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Tinykin for MultiWorld.",
        "English",
        "en_Tinykin.md",
        "setup/en",
        ["CallmeZero"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets