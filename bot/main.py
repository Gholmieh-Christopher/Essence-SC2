# Written by: Christopher Gholmieh
# Imports:

# StarCraft II:
# > Bot AI:
from sc2.bot_ai import BotAI, Race

# > Unit:
from sc2.unit import Unit

# Loguru:
# > Logger:
from loguru import logger

# Managers:
from .managers import OpponentInfoManager, DebuggingManager, ExecutionManager

from .requests import SupplyRequest
from .enumerations import RequestTypes
from sc2.ids.unit_typeid import UnitTypeId

# Classes:
class EssenceSC2(BotAI):
    # Configuration:
    RACE: Race = Race.Protoss
    NAME: str = "Essence-SC2"

    # Events:
    async def on_building_construction_started(self, structure: Unit):
        await self.ExecutionManager.on_building_construction_started(structure)

    async def on_unit_destroyed(self, unit_tag: int):
        await self.ExecutionManager.on_unit_destroyed(unit_tag)

    async def on_start(self) -> None:
        """
        Called on start of game.
        Creates manager references.
        """

        # Debugging:
        logger.info("Game initialized!")

        # Manager References:
        self.OpponentInfoManager: OpponentInfoManager = OpponentInfoManager()

        self.DebuggingManager: DebuggingManager = DebuggingManager(
            DRAW_OPPONENT_BASE_LOCATIONS=True,
            DRAW_VISIBLITY_PIXELMAP=False,
            DRAW_PLACEMENT_GRID=False,
            DRAW_PATHING_GRID=False,
            DRAW_EXPANSIONS=True,
        )

        self.ExecutionManager: ExecutionManager = ExecutionManager()

        await self.ExecutionManager.add_request(SupplyRequest(
            action_id=UnitTypeId.PROBE,
            request_type=RequestTypes.TRAIN_TYPE,
            position=None,
            supply_trigger=12,
        ))

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.TRAIN_TYPE,
            action_id=UnitTypeId.PROBE,
            position=None,
            supply_trigger=13
        ))

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.BUILD_TYPE,
            action_id=UnitTypeId.PYLON,
            position=self.main_base_ramp.protoss_wall_pylon,
            supply_trigger=14
        ))

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.BUILD_TYPE,
            action_id=UnitTypeId.GATEWAY,
            position=self.main_base_ramp.protoss_wall_buildings.pop(),
            supply_trigger=16
        ))

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.TRAIN_TYPE,
            action_id=UnitTypeId.ZEALOT,
            position=None,
            supply_trigger=16
        ))

        await self.ExecutionManager.add_request(
            SupplyRequest(
                request_type=RequestTypes.BUILD_TYPE,
                action_id=UnitTypeId.GATEWAY,
                position=self.main_base_ramp.protoss_wall_buildings.pop(),
                supply_trigger=16
            )
        )

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.TRAIN_TYPE,
            action_id=UnitTypeId.PROBE,
            position=None,
            supply_trigger=13
        ))

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.TRAIN_TYPE,
            action_id=UnitTypeId.PROBE,
            position=None,
            supply_trigger=14
        ))

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.TRAIN_TYPE,
            action_id=UnitTypeId.PROBE,
            position=None,
            supply_trigger=15
        ))

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.TRAIN_TYPE,
            action_id=UnitTypeId.ZEALOT,
            position=None,
            supply_trigger=20
        ))

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.BUILD_TYPE,
            action_id=UnitTypeId.PYLON,
            position=self.townhalls.first.position.towards(self.game_info.map_center, 7),
            supply_trigger=16
        ))

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.BUILD_TYPE,
            action_id=UnitTypeId.GATEWAY,
            position=self.townhalls.first.position.towards(self.game_info.map_center, 7).towards(self.expansion_locations_list[1].position, 5),
            supply_trigger=16,
        ))

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.BUILD_TYPE,
            action_id=UnitTypeId.GATEWAY,
            position=self.townhalls.first.position.towards(self.game_info.map_center, 7).towards(self.expansion_locations_list[2].position, 5),
            supply_trigger=16,
        ))

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.TRAIN_TYPE,
            action_id=UnitTypeId.ZEALOT,
            position=None,
            supply_trigger=18
        ))        

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.TRAIN_TYPE,
            action_id=UnitTypeId.ZEALOT,
            position=None,
            supply_trigger=20
        ))

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.TRAIN_TYPE,
            action_id=UnitTypeId.ZEALOT,
            position=None,
            supply_trigger=22
        ))

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.TRAIN_TYPE,
            action_id=UnitTypeId.ZEALOT,
            position=None,
            supply_trigger=24
        ))                

        await self.ExecutionManager.add_request(SupplyRequest(
            request_type=RequestTypes.TRAIN_TYPE,
            action_id=UnitTypeId.ZEALOT,
            position=None,
            supply_trigger=26
        ))

        self.executed: bool = False

    async def on_step(self, iteration: int) -> None:
        """
        Called every frame.
        Updates managers.
        """

        # Updating Managers:
        await self.OpponentInfoManager.update(self)
        await self.DebuggingManager.update(self)
        await self.ExecutionManager.update(self)

        await self.distribute_workers()

        if self.units.of_type(UnitTypeId.ZEALOT).amount > 4: 
            for i in self.units.of_type(UnitTypeId.ZEALOT):
                i.attack(self.enemy_start_locations[0])
            for i in self.units.of_type(UnitTypeId.PROBE):
                i.attack(self.enemy_start_locations[0])
            self.executed = True

        if self.executed is True:
            if self.can_afford(UnitTypeId.ZEALOT):
                await self.ExecutionManager.add_request(SupplyRequest(
                    request_type=RequestTypes.TRAIN_TYPE,
                    position=None,
                    action_id=UnitTypeId.ZEALOT,
                    supply_trigger=self.supply_used
                ))
