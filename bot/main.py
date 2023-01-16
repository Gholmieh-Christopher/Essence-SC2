# Written by: Christopher Gholmieh
# Imports:

# StarCraft II:
# > Bot AI:
from sc2.bot_ai import BotAI, Race

# Loguru:
# > Logger:
from loguru import logger

# Managers:
from .managers import OpponentInfoManager, DebuggingManager

# Classes:
class EssenceSC2(BotAI):
    # Configuration:
    RACE: Race = Race.Protoss
    NAME: str = "Essence-SC2"

    # Events:
    async def on_start(self) -> None:
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

    async def on_step(self, iteration: int) -> None:
        # Updating Managers:
        await self.OpponentInfoManager.update(self)
        await self.DebuggingManager.update(self)
