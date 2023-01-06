# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > Bot AI:
from sc2.bot_ai import BotAI, Race

# Loguru:
# > Logger:
from loguru import logger

# Classes:
class EssenceSC2(BotAI):
    # Configuration:
    RACE: Race = Race.Protoss
    NAME: str = "Essence-SC2"

    # Events:
    async def on_start(self) -> None:
        # Debugging:
        logger.info("Game initialized!")

    async def on_step(self, iteration: int) -> None:
        pass
