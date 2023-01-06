# Written by: Christopher Gholmieh
# Imports:

# Core:
from bot.core import Enumeration

# Classes:
class StepActions:
    BUILD_ACTION: Enumeration = Enumeration(0, "BUILD_STEP_ACTION")
    TRAIN_ACTION: Enumeration = Enumeration(1, "TRAIN_STEP_ACTION")

