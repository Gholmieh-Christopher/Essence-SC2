# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > Bot AI:
from sc2.bot_ai import BotAI, Race

# Loguru:
# > Logger:
from loguru import logger

# Managers:
from .managers import DebuggingManager

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
        self.DebuggingManager: DebuggingManager = DebuggingManager(
            DRAW_VISIBLITY_PIXELMAP=False,
            DRAW_PLACEMENT_GRID = False,
            DRAW_PATHING_GRID=False,
            DRAW_EXPANSIONS=True
        )

    async def on_step(self, iteration: int) -> None:
        # Updating Managers:
        await self.DebuggingManager.update(self)