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

# Enumerations:
from bot.enumerations import RequestTypes

# Bases:
from bot.bases import Manager, Request

# Classes:
class ExecutionManager(Manager):
    """
    Builds structures for Essence-SC2.
    Can take orders from outside sources using add_request method.

    Also stores structure positions.
    If a structure is destroyed, it will be rebuilt.
    """

    # Initialization:
    def __init__(self) -> None:
        # Dictionaries:
        self.structure_projections: typing.Dict[UnitTypeId, int] = {}
        self.structures: typing.Dict[int, typing.List[UnitTypeId, Point2]] = {}

        # Lists:
        self.verifying: list = []
        self.requests: list = []
        self.cleanup: list = []

    # Methods:
    async def add_request(self, request: Request) -> bool:
        # Guardian Statements:
        if request in self.requests:
            return False

        self.requests.append(request)
        return True

    async def update(self, AI: BotAI) -> None:
        # Executing Requests:
        for awaited_request in self.requests:
            result: bool = await awaited_request.execute(AI)

            if result is True:
                self.verifying.append(awaited_request)

                self.structure_projections[awaited_request.action_id] = (
                    self.structure_projections.get(awaited_request.action_id, 0)
                    + awaited_request.quantity
                )

        for awaited_request in self.verifying:
            if awaited_request in self.requests:
                del self.requests[self.requests.index(awaited_request)]

            if (
                AI.structures.of_type(awaited_request.action_id).amount
                >= self.structure_projections[awaited_request.action_id]
            ):
                self.cleanup.append(awaited_request)

                continue
            else:
                await awaited_request.execute(AI)

        for awaited_request in self.cleanup:
            if awaited_request in self.verifying:
                del self.verifying[self.verifying.index(awaited_request)]

        self.cleanup: list = []

    # Events:
    async def on_building_construction_started(self, structure: Unit) -> None:
        self.structures[structure.tag] = [structure.type_id, structure.position]

    async def on_unit_destroyed(self, unit_tag: int) -> None:
        # Guardian Statements:
        if unit_tag not in self.structures:
            return None

        rebuild_data: list = self.structures[unit_tag]

        self.requests.append(
            Request(
                request_type=RequestTypes.BUILD_TYPE,
                action_id=rebuild_data[0],
                position=rebuild_data[1],
                quantity=1,
            )
        )

        del self.structures[unit_tag]
