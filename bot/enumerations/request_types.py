# Written by: Christopher Gholmieh
# Imports:

# Core:
from bot.core import Enumeration

# Classes:
class RequestTypes:
    EXPAND_REQUEST: Enumeration = Enumeration(0, "EXPAND_REQUEST")
    BUILD_REQUEST: Enumeration = Enumeration(1, "BUILD_REQUEST")
    TRAIN_REQUEST: Enumeration = Enumeration(2, "TRAIN_REQUEST")
