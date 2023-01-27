# Written by: Christopher Gholmieh
# Imports:

# StarCraft II:
# > Bot AI:
from sc2.bot_ai import BotAI

# > Unit:
from sc2.unit import Unit

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
    async def on_building_construction_complete(self, structure: Unit) -> None:
        """
        Called every time a structure is finished being warped.

        :param structure:
        """

    async def on_building_construction_started(self, structure: Unit) -> None:
        """
        Called every time a structure has started to warp.

        :param structure:
        """

    async def on_unit_destroyed(self, unit_tag: int) -> None:
        """
        Meant to be overridden.
        Called when a unit is destroyed or dies.
        Structures also count as units.

        :param unit_tag:
        """
