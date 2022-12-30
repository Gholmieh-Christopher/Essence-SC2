# Written by: Christopher Gholmieh
# Imports:

# Starcraft II:
# > IDs:
from sc2.ids.unit_typeid import UnitTypeId

# Dictionaries:
PROTOSS: dict = {
    UnitTypeId.NEXUS: {UnitTypeId.PROBE},
    UnitTypeId.GATEWAY: {UnitTypeId.ZEALOT},
    UnitTypeId.CYBERNETICSCORE: {
        UnitTypeId.STALKER,
        UnitTypeId.ADEPT,
        UnitTypeId.SENTRY,
    },
    UnitTypeId.DARKSHRINE: {UnitTypeId.DARKTEMPLAR, UnitTypeId.ARCHON},
    UnitTypeId.TEMPLARARCHIVE: {UnitTypeId.HIGHTEMPLAR, UnitTypeId.ARCHON},
    UnitTypeId.ROBOTICSFACILITY: {
        UnitTypeId.IMMORTAL,
        UnitTypeId.OBSERVER,
        UnitTypeId.WARPPRISM,
    },
    UnitTypeId.ROBOTICSBAY: {UnitTypeId.COLOSSUS, UnitTypeId.DISRUPTOR},
    UnitTypeId.STARGATE: {
        UnitTypeId.VOIDRAY, 
        UnitTypeId.ORACLE,
        UnitTypeId.PHOENIX,
    },
    UnitTypeId.FLEETBEACON: {UnitTypeId.CARRIER, UnitTypeId.TEMPEST}
}
