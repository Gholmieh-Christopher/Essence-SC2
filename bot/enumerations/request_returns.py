# Written by: Christopher Gholmieh
# Imports:

# Core:
from bot.core import Enumeration

# Classes:
class RequestReturns:
    NOT_APPROPRIATE_SUPPLY: Enumeration = Enumeration(0, "NOT_APPROPRIATE_SUPPLY")
    NOT_ENOUGH_RESOURCES: Enumeration = Enumeration(1, "NOT_ENOUGH_RESOURCES")
    NOT_ENOUGH_SUPPLY: Enumeration = Enumeration(2, "NOT_ENOUGH_SUPPLY")
    POSITION_BLOCKED: Enumeration = Enumeration(3, "POSITION_BLOCKED")
    OKAY_RETURN: Enumeration = Enumeration(4, "OKAY_RETURN")
    NO_WORKER: Enumeration = Enumeration(5, "NO_WORKER")
