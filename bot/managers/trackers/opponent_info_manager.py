# Written by: Christopher Gholmieh
# Imports:

# StarCraft II:
# > Position:
from sc2.position import Point3, Point2

# > Bot AI:
from sc2.bot_ai import BotAI

# > IDs:
from sc2.ids.unit_typeid import UnitTypeId

# Typing:
import typing

# Dictionaries:
from bot.dictionaries import STRUCTURE_TRAINS, TOWNHALL_IDS

# Bases:
from bot.bases import Manager

# Classes:
class OpponentInfoManager(Manager):
    """
    Collects information on opponent:
        Defines what units they can train.
        Defines their expansion locations.

        TODO: Define ghost unit positions.
        TODO: If the enemy has a race of random, be able to identify their race by units or structures.
    """

    # Initialization:
    def __init__(self) -> None:
        # Dictionaries:
        self.opponent_expansion_locations: typing.Dict[int, Point2] = {}
        self.enemy_structure_cache: dict = {}

    # Properties:
    @property
    def EXPANSION_LOCATION_COLOR(self) -> Point3:
        return Point3((255, 0, 0))

    # Methods:
    async def update(self, AI: BotAI) -> None:
        self.possible_opponent_units: typing.Set[UnitTypeId] = set()

        for enemy_structure in AI.enemy_structures:
            # Updating Expansion Locations:
            if (
                enemy_structure.type_id in TOWNHALL_IDS
                and enemy_structure.tag not in self.opponent_expansion_locations
                and enemy_structure.position3d
                not in self.opponent_expansion_locations.values()
            ):
                self.opponent_expansion_locations[
                    enemy_structure.tag
                ] = enemy_structure.position3d
            elif (
                enemy_structure.tag in self.opponent_expansion_locations
                and enemy_structure.position
                != self.opponent_expansion_locations[enemy_structure.tag]
            ):
                self.opponent_expansion_locations[
                    enemy_structure.tag
                ] = enemy_structure.position3d

            if STRUCTURE_TRAINS.get(enemy_structure.type_id) is None:
                continue

            for unit_id in STRUCTURE_TRAINS[enemy_structure.type_id]:
                if unit_id in self.possible_opponent_units:
                    continue

                self.possible_opponent_units.add(unit_id)
