# Written by: Christopher Gholmieh
# Imports:

# StarCraft II:
# > IDs:
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.ability_id import AbilityId

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

UNIT_TO_STRUCTURE: dict = {
    # NOTE: Skipped the warpgate / gateway units because they require special functionality.
    # Protoss:
    UnitTypeId.PROBE: {UnitTypeId.NEXUS},
    # Tier Two:
    UnitTypeId.WARPPRISM: {UnitTypeId.ROBOTICSFACILITY},
    UnitTypeId.DISRUPTOR: {UnitTypeId.ROBOTICSFACILITY},
    UnitTypeId.COLOSSUS: {UnitTypeId.ROBOTICSFACILITY},
    UnitTypeId.IMMORTAL: {UnitTypeId.ROBOTICSFACILITY},
    UnitTypeId.OBSERVER: {UnitTypeId.ROBOTICSFACILITY},
    UnitTypeId.VOIDRAY: {UnitTypeId.STARGATE},
    UnitTypeId.PHOENIX: {UnitTypeId.STARGATE},
    UnitTypeId.ORACLE: {UnitTypeId.STARGATE},
    # Tier 3:
    UnitTypeId.MOTHERSHIP: {UnitTypeId.NEXUS},
    UnitTypeId.CARRIER: {UnitTypeId.STARGATE},
    UnitTypeId.TEMPEST: {UnitTypeId.STARGATE},
}

SPECIAL_UNITS: set = {
    UnitTypeId.HIGHTEMPLAR,
    UnitTypeId.DARKTEMPLAR,
    UnitTypeId.STALKER,
    UnitTypeId.ZEALOT,
    UnitTypeId.SENTRY,
    UnitTypeId.ADEPT,
}

SPECIAL_TO_WARP: dict = {
    UnitTypeId.HIGHTEMPLAR: AbilityId.WARPGATETRAIN_HIGHTEMPLAR,
    UnitTypeId.DARKTEMPLAR: AbilityId.WARPGATETRAIN_DARKTEMPLAR,
    UnitTypeId.STALKER: AbilityId.WARPGATETRAIN_STALKER,
    UnitTypeId.ZEALOT: AbilityId.WARPGATETRAIN_ZEALOT,
    UnitTypeId.SENTRY: AbilityId.WARPGATETRAIN_SENTRY,
    UnitTypeId.ADEPT: AbilityId.TRAINWARP_ADEPT,
}
