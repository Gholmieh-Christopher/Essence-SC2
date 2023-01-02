# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > Position:
from sc2.position import Point2

# > Bot AI:
from sc2.bot_ai import BotAI

# > Units:
from sc2.units import Units

# > IDs:
from sc2.ids.unit_typeid import UnitTypeId

# Typing:
import typing

# Enumerations:
from bot.enumerations import RequestReturns, RequestTypes

# Dictionaries:
from bot.dictionaries import PROTOSS_UNIT_LINKS, WARPGATE_UNITS

# Core:
from bot.core import Enumeration

# Classes:
class QuantityRequest:
    # Initialization:
    def __init__(
            self, supply_trigger: int, request_type: Enumeration, action_id: UnitTypeId, position: typing.Optional[Point2]
    ) -> None:
        # Integers:
        self.supply_trigger: int = supply_trigger

        # Miscellaneous:
        self.request_type: Enumeration = request_type
        self.action_id: UnitTypeId = action_id
        self.position: typing.Optional[Point2] = position

    # Methods:
    async def execute(self, AI: BotAI) -> Enumeration:
        # Guardian Statements:
        if (AI.supply_army + AI.supply_workers) != self.supply_trigger:
            return RequestReturns.NOT_APPROPRIATE_SUPPLY

        if AI.can_afford(self.action_id) is False:
            return RequestReturns.NOT_ENOUGH_RESOURCES

        if self.request_type == RequestTypes.TRAIN_REQUEST:
            if self.action_id in WARPGATE_UNITS:
                # TODO: Make it function for warpgate units and gateway units, should be easy.
                return RequestReturns.OKAY_RETURN

            structure_links: set = PROTOSS_UNIT_LINKS[self.action_id]

            structures: Units = AI.structures.of_type(structure_links).ready

            for structure in structures:
                structure.train(self.action_id)

                break

        return RequestReturns.OKAY_RETURN
