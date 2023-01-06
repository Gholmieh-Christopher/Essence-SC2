# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > Bot AI:
from sc2.bot_ai import BotAI, Race

# Loguru:
# > Logger:
from loguru import logger

# Managers:
from .managers import DebuggerManager, GameInfoManager, StepManager

# Classes:
class EssenceSC2(BotAI):
    # Configuration:
    RACE: Race = Race.Protoss
    NAME: str = "Essence-SC2"

    # Functions:
    async def on_start(self) -> None:
        # Manager References:
        self.DebuggerManager: DebuggerManager = DebuggerManager(self)
        self.GameInfoManager: GameInfoManager = GameInfoManager(self)
        self.StepManager: StepManager = StepManager(self.GameInfoManager, self)

        # Debugging:
        logger.info("Game initialized!")

    async def on_step(self, iteration: int) -> None:
        # Managers:
        self.DebuggerManager.update(self)
        self.GameInfoManager.update(self)

        await self.StepManager.update(self)

    # Methods:
    async def on_unit_destroyed(self, unit_tag: int):
        self.GameInfoManager.on_unit_destroyed(unit_tag)
