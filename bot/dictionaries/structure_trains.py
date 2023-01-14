# Written by: Christopher Gholmieh
# Imports:

# StarCraft II:
# > IDs:
from sc2.ids.unit_typeid import UnitTypeId

# Dictionaries:
STRUCTURE_TRAINS: dict = {
    # Protoss:
    UnitTypeId.NEXUS: {UnitTypeId.PROBE},
    # Tier 1:
    UnitTypeId.GATEWAY: {UnitTypeId.ZEALOT},
    # Tier: 1.5:
    UnitTypeId.CYBERNETICSCORE: {
        UnitTypeId.STALKER,
        UnitTypeId.SENTRY,
        UnitTypeId.ADEPT,
    },
    # Tier 2:
    UnitTypeId.ROBOTICSFACILITY: {
        UnitTypeId.WARPPRISM,
        UnitTypeId.IMMORTAL,
        UnitTypeId.OBSERVER,
    },
    UnitTypeId.ROBOTICSBAY: {
        UnitTypeId.DISRUPTOR,
        UnitTypeId.COLOSSUS,
    },
    UnitTypeId.STARGATE: {
        UnitTypeId.VOIDRAY,
        UnitTypeId.PHOENIX,
        UnitTypeId.ORACLE,
    },
    # Tier 3:
    UnitTypeId.TEMPLARARCHIVE: {UnitTypeId.HIGHTEMPLAR},
    UnitTypeId.DARKSHRINE: {UnitTypeId.DARKTEMPLAR},
    UnitTypeId.FLEETBEACON: {
        UnitTypeId.MOTHERSHIP,
        UnitTypeId.CARRIER,
        UnitTypeId.TEMPEST,
    },
}
