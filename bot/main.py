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
from .managers import OpponentInfoManager, DebuggingManager, BuildingManager

# Classes:
class EssenceSC2(BotAI):
    # Configuration:
    RACE: Race = Race.Protoss
    NAME: str = "Essence-SC2"

    # Events:
    async def on_building_construction_started(self, structure: Unit):
        await self.BuildingManager.on_building_construction_started(structure)

    async def on_unit_destroyed(self, unit_tag: int):
        await self.BuildingManager.on_unit_destroyed(unit_tag)

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

        self.BuildingManager: BuildingManager = BuildingManager()

    async def on_step(self, iteration: int) -> None:
        """
        Called every frame.
        Updates managers.
        """

        # Updating Managers:
        await self.OpponentInfoManager.update(self)
        await self.DebuggingManager.update(self)
        await self.BuildingManager.update(self)
