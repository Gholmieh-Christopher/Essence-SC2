# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > Bot AI:
from sc2.bot_ai import BotAI, Race

# Loguru:
# > Logger:
from loguru import logger

# Managers:
from .managers import DebuggerManager, GameInfoManager

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

        # Debugging:
        logger.info("Game initialized!")

    async def on_step(self, iteration: int) -> None:
        # Managers:
        self.DebuggerManager.update(self)
        self.GameInfoManager.update(self)

    async def on_enemy_unit_entered_vision(self, unit):
        print(unit.tag)

