# Written by: Christopher Gholmieh
# Imports:

# StarCraft II:
# > Position:
from sc2.position import Point2

# > IDs:
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId

# Dataclasses:
import dataclasses

# Typing:
import typing

# Bases:
from bot.bases import Enumeration

# Classes:
@dataclasses.dataclass
class Request:
    """
    Base class for requests.

    :param request_type:
    :param action_id:
    :param position:
    :param quantity:
    """

    request_type: Enumeration

    action_id: typing.Union[UnitTypeId, UpgradeId]

    position: typing.Optional[Point2]

    quantity: int
