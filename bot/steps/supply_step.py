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
from sc2.ids.ability_id import AbilityId

# Dictionaries:
from bot.dictionaries import PROTOSS_UNIT_LINKS, WARPGATE_UNITS

# Dataclasses:
from dataclasses import dataclass

# Typing:
import typing

# Enumerations:
from bot.enumerations import StepActions, StepReturns

# Core:
from bot.core import Enumeration

# Classes:
@dataclass
class SupplyStep:
    # Integers:
    supply_trigger: int
    quantity: int
    amount: int

    # Booleans:
    queue: bool

    # Miscellaneous:
    step_action: Enumeration
    action_id: typing.Union[UnitTypeId, AbilityId]

    # Lists:
    positions: typing.Union[typing.List, Point2, None]

    # Methods:
    async def execute(self, AI: BotAI) -> Enumeration:
        # Guardian Statements:
        if AI.can_afford(self.action_id) is False:
            return StepReturns.NOT_ENOUGH_RESOURCES_RETURN

        if (
            AI.supply_army + AI.supply_workers + AI.already_pending(self.action_id)
        ) != self.supply_trigger:
            return StepReturns.NOT_APPROPRIATE_SUPPLY_RETURN

        # Train Request:
        if self.step_action == StepActions.TRAIN_ACTION:
            if self.action_id not in WARPGATE_UNITS:

                structures: Units = AI.structures.of_type(
                    PROTOSS_UNIT_LINKS[self.action_id]
                ).ready

                if not any(structures):
                    return StepReturns.NO_STRUCTURE_TO_PRODUCE_UNIT_RETURN

                for iteration in range(self.quantity):
                    if self.amount > self.quantity:
                        break

                    if not any(structures.idle):
                        structures.random.train(self.action_id, queue=self.queue)
                    else:
                        structures.idle.random.train(self.action_id, queue=self.queue)

                    self.amount += 1

                return StepReturns.SUCCESSFUL_RETURN
