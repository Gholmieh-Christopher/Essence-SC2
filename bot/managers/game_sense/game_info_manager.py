# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > Bot AI:
from sc2.bot_ai import BotAI, Race

# > IDs:
from sc2.ids.unit_typeid import UnitTypeId

# Managers:
class GameInfoManager:
    # Initialization:
    def __init__(self, AI: BotAI) -> None:
        # Miscellaneous:
        self.AI: BotAI = AI

        self.enemy_race: Race = AI.enemy_race

    # Functions:
    def update(self, AI: BotAI) -> None:
        # Updating Variables:
        self.AI: BotAI = AI

        # Calling Methods:
        if self.enemy_race == Race.Random:
            self.identify_race()

    # Methods:
    def identify_race(self) -> None:
        for enemy_structure in self.AI.enemy_structures:
            self.enemy_race = enemy_structure.race

            break

        for enemy_unit in self.AI.enemy_units:
            self.enemy_race = enemy_unit.race

            break

