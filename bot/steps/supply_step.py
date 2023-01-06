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
from sc2.ids.upgrade_id import UpgradeId
from sc2.ids.ability_id import AbilityId

# Dictionaries:
from bot.dictionaries import PROTOSS_UNIT_LINKS, WARPGATE_UNITS, UNIT_TO_WARP

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
    positions: typing.Optional[typing.Union[typing.List, Point2]]

    # Methods:
    async def execute(self, AI: BotAI) -> Enumeration:
        # Guardian Statements:
        if AI.can_afford(self.action_id) is False:
            return StepReturns.NOT_ENOUGH_RESOURCES_RETURN

        # Train Request:
        if self.step_action == StepActions.TRAIN_ACTION:
            # Guardian Statement:
            if (
                AI.supply_army + AI.supply_workers + AI.already_pending(self.action_id)
            ) != self.supply_trigger and self.amount == 0:
                return StepReturns.NOT_APPROPRIATE_SUPPLY_RETURN

            if self.action_id not in WARPGATE_UNITS:

                structures: Units = AI.structures.of_type(
                    PROTOSS_UNIT_LINKS[self.action_id]
                ).ready
                if not any(structures):
                    return StepReturns.NO_STRUCTURE_TO_PRODUCE_UNIT_RETURN

                for iteration in range(self.quantity):
                    if self.amount >= self.quantity:
                        break

                    if AI.can_afford(self.action_id) is False:
                        return StepReturns.NOT_ENOUGH_RESOURCES_RETURN

                    if not any(structures.idle):
                        structures.random.train(self.action_id, queue=self.queue)
                    else:
                        structures.idle.random.train(self.action_id, queue=self.queue)

                    self.amount += 1

                    return StepReturns.SUCCESSFUL_RETURN

            elif self.action_id in WARPGATE_UNITS:
                if UpgradeId.WARPGATERESEARCH in AI.state.upgrades:
                    structures: Units = AI.structures.of_type(UnitTypeId.WARPGATE).ready
                    if not any(structures):
                        return StepReturns.NO_STRUCTURE_TO_PRODUCE_UNIT_RETURN

                    for iteration in range(self.quantity):
                        if self.amount >= self.quantity:
                            break

                        if AI.can_afford(self.action_id) is False:
                            return StepReturns.NOT_ENOUGH_RESOURCES_RETURN

                        for warpgate in structures:
                            abilities = AI.get_available_abilities(warpgate)

                            if UNIT_TO_WARP[self.action_id] in abilities:
                                if isinstance(self.positions, list):
                                    position: Point2 = self.positions.pop()
                                    
                                    position = await AI.find_placement(UNIT_TO_WARP[self.action_id], position)
                                    if position is None:
                                        return StepReturns.POSITION_BLOCKED_RETURN

                                    warpgate.warp_in(self.action_id, position)
                                    
                                    self.amount += 1
                                    return StepReturns.SUCCESSFUL_RETURN

                                elif isinstance(self.positions, Point2):
                                    position: Point2 = await AI.find_placement(UNIT_TO_WARP[self.action_id], position)
                                    if position is None:
                                        return StepReturns.POSITION_BLOCKED_RETURN

                                    warpgate.warp_in(self.action_id, position)
                                    
                                    self.amount += 1
                                    return StepReturns.SUCCESSFUL_RETURN
                                
                                elif isinstance(self.positions, None):
                                    pylons: Units = AI.structures.of_type(UnitTypeId.PYLON)
                                    if not any(pylons):
                                        return StepReturns.NO_STRUCTURE_TO_PRODUCE_UNIT_RETURN

                                    position: Point2 = await AI.find_placement(UNIT_TO_WARP[self.action_id], pylons.random.position)

                                    if position is None:
                                        return StepReturns.POSITION_BLOCKED_RETURN

                                    warpgate.warp_in(self.action_id, position)
                                    
                                    self.amount += 1
                                    return StepReturns.SUCCESSFUL_RETURN
                else:
                    structures: Units = AI.structures.of_type(UnitTypeId.GATEWAY).ready
                    if not any(structures):
                        return StepReturns.NO_STRUCTURE_TO_PRODUCE_UNIT_RETURN

                    for iteration in range(self.quantity):
                        if self.amount >= self.quantity:
                            break

                        if AI.can_afford(self.action_id) is False:
                            return StepReturns.NOT_ENOUGH_RESOURCES_RETURN

                        if not any(structures.idle):
                            structures.random.train(self.action_id, queue=self.queue)
                        else:
                            structures.idle.random.train(self.action_id, queue=self.queue)

                        self.amount += 1

                        return StepReturns.SUCCESSFUL_RETURN
