# Written by: Christopher Gholmieh
# Imports:

# StarCraft II:
# > Positions:
from sc2.position import Point2

# > Bot AI:
from sc2.bot_ai import BotAI, Race

# > Unit:
from sc2.unit import Unit

# > IDs:
from sc2.ids.unit_typeid import UnitTypeId

# Typing:
import typing

# Sequences:
from .sequences import DoubleGate

# Managers:
# > Trackers:
from bot.managers.trackers import OpponentInfoManager

# Bases:
from bot.bases import Manager

# Classes:
class BuildingManager(Manager):
    """
    Builds structures for Essence-SC2.
    Can take orders from outside sources using queue method.

    Also stores structure positions.
    If a structure is destroyed, it will be rebuilt.

    TODO: Create request inherit classes.
    TODO: Make this build stuff.
    TODO: Make this rebuild stuff.
    """

    # Initialization:
    def __init__(self, OpponentInfoManager: OpponentInfoManager) -> None:
        # Miscellaneous:
        self.OpponentInfoManager: OpponentInfoManager = OpponentInfoManager
        self.sequence = DoubleGate().sequential_list

        # Dictionaries:
        self.structures: typing.Dict[int, typing.List[UnitTypeId, Point2]] = {}

        # Lists:
        self.rebuild_queue: list = []

    # Properties:
    @property
    def matchup_to_build(self) -> dict:
        return {Race.Protoss: [DoubleGate]}

    # Methods:
    async def update(self, AI: BotAI) -> None:
        pass

    # Events:
    async def on_building_construction_started(self, structure: Unit) -> None:
        self.structures[structure.tag] = [structure.type_id, structure.position]

    async def on_unit_destroyed(self, unit_tag: int) -> None:
        # Guardian Statements:
        if unit_tag not in self.structures:
            return None

        self.rebuild_queue.append(self.structures[unit_tag])
        del self.structures[unit_tag]
