# Written by: Christopher Gholmieh
# Imports:

# Core:
from bot.core import Enumeration

# Classes:
class StepReturns:
    NO_STRUCTURE_TO_PRODUCE_UNIT_RETURN: Enumeration = Enumeration(
        0, "NOT_ENOUGH_RESOURCES_RETURN"
    )
    NOT_APPROPRIATE_SUPPLY_RETURN: Enumeration = Enumeration(
        1, "NOT_APPROPRIATE_SUPPLY_RETURN"
    )
    NOT_ENOUGH_RESOURCES_RETURN: Enumeration = Enumeration(
        2, "NOT_ENOUGH_RESOURCES_RETURN"
    )
    SUCCESSFUL_RETURN: Enumeration = Enumeration(3, "SUCCESSFUL_RETURN")
    POSITION_BLOCKED_RETURN: Enumeration = Enumeration(4, "POSITION_BLOCKED_RETURN")
