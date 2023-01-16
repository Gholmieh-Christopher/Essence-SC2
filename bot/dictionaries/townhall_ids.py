# Written by: Christopher Gholmieh
# Imports:

# StarCraft II:
# > IDs:
from sc2.ids.unit_typeid import UnitTypeId

# Typing:
import typing

# Sets:
TOWNHALL_IDS: typing.Set[UnitTypeId] = {
    UnitTypeId.PLANETARYFORTRESS,
    UnitTypeId.ORBITALCOMMAND,
    UnitTypeId.COMMANDCENTER,
    UnitTypeId.HATCHERY,
    UnitTypeId.NEXUS,
}
