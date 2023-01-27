# Written by: Christopher Gholmieh
# Imports:

# StarCraft II:
# > IDs:
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId

# Dataclasses:
import dataclasses

# Typing:
import typing

# Classes:
@dataclasses.dataclass
class Request:
    """
    Base class for requests.
    """

    action_id: typing.Union[UnitTypeId, UpgradeId]

    quantity: int = 1
