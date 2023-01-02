# Written by: Christopher Gholmieh
# Imports:

# Core:
from bot.core import Enumeration

# Classes:
class RequestReturns:
    NOT_APPROPRIATE_SUPPLY: Enumeration = Enumeration(0, "NOT_APPROPRIATE_SUPPLY")
    NOT_ENOUGH_RESOURCES: Enumeration = Enumeration(1, "NOT_ENOUGH_RESOURCES")
    POSITION_BLOCKED: Enumeration = Enumeration(2, "POSITION_BLOCKED")
    OKAY_RETURN: Enumeration = Enumeration(3, "OKAY_RETURN")
