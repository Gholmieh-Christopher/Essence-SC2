# Written by: Christopher Gholmieh
# Imports:

# StarCraft II:
# > Position:
from sc2.position import Point2

# > Bot AI:
from sc2.bot_ai import BotAI

# > IDs:
from sc2.ids.unit_typeid import UnitTypeId

# Typing:
import typing

# Dictionaries:
from bot.dictionaries import STRUCTURE_TRAINS

# Bases:
from bot.bases import Manager

# Classes:
class OpponentInfoManager(Manager):
    """
    Collects information on opponent:
        Defines what units they can train.
        Defines their expansion locations.

        TODO: Define ghost unit positions.
    """

    # Initialization:
    def __init__(self, debug: bool = False) -> None:
        # Dictionaries:
        self.opponent_expansion_locations: typing.Dict[int, Point2] = {}
        self.enemy_structure_cache: dict = {}

        # Booleans:
        self.debug: bool = debug

        # Sets:
        self.townhall_ids: typing.Set[UnitTypeId] = {
            UnitTypeId.PLANETARYFORTRESS,
            UnitTypeId.ORBITALCOMMAND,
            UnitTypeId.COMMANDCENTER,
            UnitTypeId.HATCHERY,
            UnitTypeId.NEXUS,
        }

    # Methods:
    async def update(self, AI: BotAI) -> None:
        self.possible_opponent_units: typing.Set[UnitTypeId] = set()

        for enemy_structure in AI.enemy_structures:
            # Updating Expansion Locations:
            if (
                enemy_structure.type_id in self.townhall_ids
                and enemy_structure.tag not in self.opponent_expansion_locations
                and enemy_structure.position
                not in self.opponent_expansion_locations.values()
            ):
                self.opponent_expansion_locations[
                    enemy_structure.tag
                ] = enemy_structure.position
            elif (
                enemy_structure.tag in self.opponent_expansion_locations
                and enemy_structure.position
                != self.opponent_expansion_locations[enemy_structure.tag]
            ):
                self.opponent_expansion_locations[
                    enemy_structure.tag
                ] = enemy_structure.position

            if STRUCTURE_TRAINS.get(enemy_structure.type_id) is None:
                continue

            for unit_id in STRUCTURE_TRAINS[enemy_structure.type_id]:
                if unit_id in self.possible_opponent_units:
                    continue

                self.possible_opponent_units.add(unit_id)

        if self.debug is True:
            print("Possible opponent units:", self.possible_opponent_units)
            print("Enemy townhall locations:", self.opponent_expansion_locations)
            print("------------------------------------------------------------")
