# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > IDs:
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.ability_id import AbilityId

# Enumerations:
from bot.enumerations import StepActions

# Steps:
from bot.steps import SupplyStep

# Classes:
class DoubleGatePVP:
    # Initialization:
    def __init__(self) -> None:
        pass

    # Properties:
    @property
    def sequence(self) -> list:
        return [
            SupplyStep(
                12, 1, 0, False, StepActions.TRAIN_ACTION, UnitTypeId.PROBE, None
            ),
            SupplyStep(
                13, 1, 0, False, StepActions.TRAIN_ACTION, UnitTypeId.ZEALOT, None
            ),
        ]
