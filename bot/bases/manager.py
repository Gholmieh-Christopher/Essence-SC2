# Written by: Christopher Gholmieh
# Imports:

# StarCraft II:
# > Bot AI:
from sc2.bot_ai import BotAI

# Classes:
class Manager:
    """
    Base class for managers.
    """
    
    # Methods:
    async def update(self, AI: BotAI) -> None:
        """
        Meant to be overridden.
        Called every frame.
        """
    
    # Events:
    async def on_unit_destroyed(self, unit_tag: int) -> None:
        """
        Meant to be overridden.
        Called when a unit is destroyed or dies.
        Structures also count as units.
        
        :param unit_tag:
        """
