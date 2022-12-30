# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > Bot AI:
from sc2.bot_ai import BotAI, Race

# Dictionaries:
from bot.dictionaries import PROTOSS

# Managers:
class GameInfoManager:
    # Configuration:
    REGISTRY: dict = {
        Race.Protoss: PROTOSS,
    }

    # Initialization:
    def __init__(self, AI: BotAI) -> None:
        # Miscellaneous:
        self.AI: BotAI = AI

        self.enemy_race: Race = AI.enemy_race

        # Dictionaries:
        self.enemy_structure_cache: dict = {}

        # Sets:
        self.enemy_can_produce: set = set()

    # Functions:
    def update(self, AI: BotAI) -> None:
        # Updating Variables:
        self.AI: BotAI = AI

        # Calling Methods:
        if self.enemy_race == Race.Random:
            self.identify_race()

        self.update_enemy_production()

        print("-----------------------------------------------")
        print(self.enemy_can_produce)

    # Methods:
    def update_enemy_production(self) -> None:
        for enemy_structure in self.AI.enemy_structures:
            key = (
                enemy_structure.tech_alias
                if enemy_structure.tech_alias is not None
                else enemy_structure.type_id
            )

            if self.REGISTRY[self.enemy_race].get(key) is None:
                continue

            self.enemy_structure_cache[enemy_structure.tag] = key

            for enemy_unit_id in self.REGISTRY[self.enemy_race][key]:
                self.enemy_can_produce.add(enemy_unit_id)

    def on_unit_destroyed(self, unit_tag: int) -> None:
        if unit_tag not in self.enemy_structure_cache:
            return None

        key = self.enemy_structure_cache[unit_tag]

        for enemy_unit_id in self.REGISTRY[self.enemy_race][key]:
            self.enemy_can_produce.remove(enemy_unit_id)

    def identify_race(self) -> None:
        for enemy_structure in self.AI.enemy_structures:
            self.enemy_race = enemy_structure.race

            break

        for enemy_unit in self.AI.enemy_units:
            self.enemy_race = enemy_unit.race

            break
