# Written by: Christopher Gholmieh
# Imports:

# StarCraft II:
# > Position:
from sc2.position import Point2

# > Bot AI:
from sc2.bot_ai import BotAI

# > Units:
from sc2.units import Units

# > Unit:
from sc2.unit import Unit

# > IDs:
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId

# Dataclasses:
import dataclasses

# Typing:
import typing

# Dictionaries:
from bot.dictionaries import UNIT_TO_STRUCTURE, SPECIAL_UNITS, SPECIAL_TO_WARP

# Enumerations:
from bot.enumerations import RequestTypes

# Bases:
from bot.bases import Request

# Classes:
@dataclasses.dataclass
class SupplyRequest(Request):
    """
    A request that fires when the supply trigger is hit.

    TODO: Finish dictionaries/structure_trains.py and organize it more.

    :param supply_trigger:
    """

    supply_trigger: int = 12

    # Methods:
    async def execute(self, AI: BotAI) -> bool:
        # Guardian Statements:
        if (
            AI.supply_used != self.supply_trigger
            and self._valid_attempts == 0
            and self.attempted is False
        ):
            return False

        if AI.can_afford(self.action_id) is False:
            return False

        # Main:
        self.attempted = True

        match self.request_type:
            case RequestTypes.TRAIN_TYPE:
                options: set = UNIT_TO_STRUCTURE[self.action_id]

                structures: Units = AI.structures.of_type(options)
                if not any(structures):
                    return False

                for iteration in range(self.quantity):
                    if self._valid_attempts == self.quantity:
                        return True

                    if (
                        self.action_id in SPECIAL_UNITS
                        and UpgradeId.WARPGATERESEARCH in AI.state.upgrades
                    ):
                        position: typing.Optional[Point2] = self.position

                        if position is None:
                            pylons: Units = AI.structures.of_type(UnitTypeId.PYLON)
                            if not any(pylons):
                                return False

                        position = AI.find_placement(self.action_id, near=position)
                        if position is None:
                            return False

                        warpgates: Units = AI.structures.of_type(
                            UnitTypeId.WARPGATE
                        ).ready.filter(
                            lambda warpgate: SPECIAL_TO_WARP[self.action_id]
                            in AI.get_available_abilities(warpgate)
                        )
                        if not any(warpgates):
                            return False

                        warpgates.random.warp_in(self.action_id, position)

                        self._valid_attempts += 1
                    else:

                        structure = None

                        idle_structures: Units = structures.filter(
                            lambda structure: structure.is_idle
                        )

                        if not any(idle_structures):
                            structure = structures.random
                        else:
                            structure = idle_structures.random

                        structure.train(self.action_id)

                        self._valid_attempts += 1

                        return True

            case RequestTypes.BUILD_TYPE:
                if self._valid_attempts == self.quantity:
                    return True

                position: typing.Union[typing.Callable, Point2] = self.position
                if isinstance(position, Point2) is False:
                    position = position(AI)

                position: Point2 = await AI.find_placement(
                    self.action_id, near=position
                )

                if position is None:
                    return False

                # TODO: Add a filter.
                worker: typing.Optional[Unit] = AI.workers.closest_to(position)
                if worker is None:
                    return False

                worker.build(self.action_id, position)

                self._valid_attempts += 1

                return True
