# Written by: Christopher Gholmieh
# Imports:

from sc2.bot_ai import BotAI

# StarCraft II:
# > IDs:
from sc2.ids.unit_typeid import UnitTypeId

# Enumerations:
from bot.enumerations import RequestTypes

# Requests:
from bot.requests import SupplyRequest

# Classes:
class DoubleGate:
    # Initialization:
    def __init__(self) -> None:
        pass

    # Properties:
    @property
    def sequential_list(self) -> list:
        return [
            SupplyRequest(
                request_type=RequestTypes.BUILD_TYPE,
                action_id=UnitTypeId.PYLON,
                position=lambda AI: AI.main_base_ramp.protoss_wall_pylon,
                quantity=1,
                supply_trigger=12,
            )
        ]
