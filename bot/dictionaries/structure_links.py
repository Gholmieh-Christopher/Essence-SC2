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

TERRAN: dict = {
    UnitTypeId.COMMANDCENTER: {UnitTypeId.SCV},
    UnitTypeId.BARRACKS: {UnitTypeId.MARINE, UnitTypeId.REAPER},
    UnitTypeId.BARRACKSTECHLAB: {
        UnitTypeId.MARINE,
        UnitTypeId.REAPER,
        UnitTypeId.MARAUDER,
    },
    UnitTypeId.BARRACKSREACTOR: {UnitTypeId.MARINE, UnitTypeId.REAPER},
    UnitTypeId.GHOSTACADEMY: {UnitTypeId.GHOST},
    UnitTypeId.FACTORY: {UnitTypeId.HELLION, UnitTypeId.WIDOWMINE},
    UnitTypeId.FACTORYTECHLAB: {
        UnitTypeId.HELLION,
        UnitTypeId.WIDOWMINE,
        UnitTypeId.CYCLONE,
        UnitTypeId.SIEGETANK,
    },
    UnitTypeId.FACTORYREACTOR: {UnitTypeId.HELLION, UnitTypeId.WIDOWMINE},
    UnitTypeId.ARMORY: {UnitTypeId.HELLIONTANK, UnitTypeId.THOR},
    UnitTypeId.STARPORT: {
        UnitTypeId.LIBERATOR,
        UnitTypeId.MEDIVAC,
        UnitTypeId.VIKING,
    },
    UnitTypeId.STARPORTTECHLAB: {
        UnitTypeId.LIBERATOR,
        UnitTypeId.MEDIVAC,
        UnitTypeId.VIKING,
        UnitTypeId.RAVEN,
        UnitTypeId.BANSHEE,
    },
    UnitTypeId.STARPORTREACTOR: {
        UnitTypeId.LIBERATOR,
        UnitTypeId.MEDIVAC,
        UnitTypeId.VIKING,
    },
    UnitTypeId.FUSIONCORE: {UnitTypeId.BATTLECRUISER}
}
