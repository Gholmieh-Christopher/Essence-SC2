# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > IDs:
from sc2.ids.unit_typeid import UnitTypeId

# Dictionaries:
PROTOSS_UNIT_LINKS: dict = {UnitTypeId.PROBE: {UnitTypeId.NEXUS}}

WARPGATE_UNITS: set = set({
    UnitTypeId.ZEALOT,
    UnitTypeId.STALKER,
    UnitTypeId.SENTRY,
    UnitTypeId.ADEPT,
    UnitTypeId.DARKTEMPLAR,
    UnitTypeId.HIGHTEMPLAR
})
