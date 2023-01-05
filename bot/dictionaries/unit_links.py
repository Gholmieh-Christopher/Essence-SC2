# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > IDs:
from sc2.ids.unit_typeid import UnitTypeId

# Dictionaries:
PROTOSS_UNIT_LINKS: dict = {
    UnitTypeId.PROBE: {UnitTypeId.NEXUS},
    UnitTypeId.ZEALOT: {UnitTypeId.WARPGATE, UnitTypeId.GATEWAY},
    UnitTypeId.STALKER: {UnitTypeId.WARPGATE, UnitTypeId.GATEWAY},
    UnitTypeId.SENTRY: {UnitTypeId.WARPGATE, UnitTypeId.GATEWAY},
    UnitTypeId.DARKTEMPLAR: {UnitTypeId.WARPGATE, UnitTypeId.GATEWAY},
    UnitTypeId.HIGHTEMPLAR: {UnitTypeId.WARPGATE, UnitTypeId.GATEWAY},
    UnitTypeId.OBSERVER: {UnitTypeId.ROBOTICSFACILITY},
    UnitTypeId.IMMORTAL: {UnitTypeId.ROBOTICSFACILITY},
    UnitTypeId.WARPPRISM: {UnitTypeId.ROBOTICSFACILITY},
    UnitTypeId.COLOSSUS: {UnitTypeId.COLOSSUS},
    UnitTypeId.DISRUPTOR: {UnitTypeId.DISRUPTOR},
    UnitTypeId.VOIDRAY: {UnitTypeId.STARGATE},
    UnitTypeId.PHOENIX: {UnitTypeId.STARGATE},
    UnitTypeId.ORACLE: {UnitTypeId.STARGATE},
    UnitTypeId.TEMPEST: {UnitTypeId.STARGATE},
    UnitTypeId.CARRIER: {UnitTypeId.CARRIER},
}

WARPGATE_UNITS: set = set(
    {
        UnitTypeId.ZEALOT,
        UnitTypeId.STALKER,
        UnitTypeId.SENTRY,
        UnitTypeId.ADEPT,
        UnitTypeId.DARKTEMPLAR,
        UnitTypeId.HIGHTEMPLAR,
    }
)