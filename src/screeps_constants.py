__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
# Don't actually include any of the following lines:
__pragma__('skip')
# This file defines names that we expect to exist in screeps.
# TODO: make each of these a full class, for full autocomplete.
__all__ = [
    # Classes
    "Creep",
    "Game",
    "Memory",
    "Room",
    "RoomPosition",
    "PathFinder",
    "Object",
    "Math",
    # Constants
    "OK",
    "CONTROLLER_STRUCTURES",
    "ERR_NO_PATH",
    "ERR_NOT_FOUND",
    "ERR_NOT_IN_RANGE",
    "ERR_FULL",
    "ERR_INVALID_TARGET",
    "ERR_NOT_ENOUGH_RESOURCES",
    "ERR_INVALID_ARGS",
    "ERR_NO_BODYPART",
    "ERR_TIRED",
    "FIND_EXIT_TOP",
    "FIND_EXIT_RIGHT",
    "FIND_EXIT_BOTTOM",
    "FIND_EXIT_LEFT",
    "FIND_EXIT",
    "FIND_CREEPS",
    "FIND_MY_CREEPS",
    "FIND_HOSTILE_CREEPS",
    "FIND_SOURCES_ACTIVE",
    "FIND_SOURCES",
    "FIND_DROPPED_ENERGY",
    "FIND_DROPPED_RESOURCES",
    "FIND_STRUCTURES",
    "FIND_MY_STRUCTURES",
    "FIND_HOSTILE_STRUCTURES",
    "FIND_FLAGS",
    "FIND_CONSTRUCTION_SITES",
    "FIND_MY_SPAWNS",
    "FIND_HOSTILE_SPAWNS",
    "FIND_MY_CONSTRUCTION_SITES",
    "FIND_HOSTILE_CONSTRUCTION_SITES",
    "FIND_MINERALS",
    "FIND_NUKES",
    "LOOK_CREEPS",
    "LOOK_TERRAIN",
    "LOOK_STRUCTURES",
    "LOOK_FLAGS",
    "LOOK_SOURCES",
    "LOOK_MINERALS",
    "LOOK_RESOURCES",
    "LOOK_CONSTRUCTION_SITES",
    "STRUCTURE_SPAWN",
    "STRUCTURE_EXTENSION",
    "STRUCTURE_ROAD",
    "STRUCTURE_WALL",
    "STRUCTURE_RAMPART",
    "STRUCTURE_KEEPER_LAIR",
    "STRUCTURE_PORTAL",
    "STRUCTURE_CONTROLLER",
    "STRUCTURE_LINK",
    "STRUCTURE_STORAGE",
    "STRUCTURE_TOWER",
    "STRUCTURE_OBSERVER",
    "STRUCTURE_POWER_BANK",
    "STRUCTURE_POWER_SPAWN",
    "STRUCTURE_EXTRACTOR",
    "STRUCTURE_LAB",
    "STRUCTURE_TERMINAL",
    "STRUCTURE_CONTAINER",
    "STRUCTURE_NUKER",
    "RESOURCE_ENERGY",
    "RESOURCE_POWER",
    "RESOURCE_HYDROGEN",
    "RESOURCE_OXYGEN",
    "RESOURCE_UTRIUM",
    "RESOURCE_LEMERGIUM",
    "RESOURCE_KEANIUM",
    "RESOURCE_ZYNTHIUM",
    "RESOURCE_CATALYST",
    "RESOURCE_GHODIUM",
    "TERRAIN_MASK_WALL",
    "TERRAIN_MASK_LAVA",
    "TOP",
    "TOP_RIGHT",
    "RIGHT",
    "BOTTOM_RIGHT",
    "BOTTOM",
    "BOTTOM_LEFT",
    "LEFT",
    "TOP_LEFT",
    "MOVE",
    "WORK",
    "CARRY",
    "ATTACK",
    "RANGED_ATTACK",
    "TOUGH",
    "HEAL",
    "CLAIM",
    "BODYPART_COST",
    "BOOSTS",
    "COLOR_RED",
    "COLOR_PURPLE",
    "COLOR_BLUE",
    "COLOR_CYAN",
    "COLOR_GREEN",
    "COLOR_YELLOW",
    "COLOR_ORANGE",
    "COLOR_BROWN",
    "COLOR_GREY",
    "COLOR_WHITE",
    "ORDER_BUY",
    "ORDER_SELL",
    "CREEP_LIFE_TIME",
    "CREEP_CLAIM_LIFE_TIME",
    "CREEP_CORPSE_RATE",
    "CARRY_CAPACITY",
    "HARVEST_POWER",
    "HARVEST_MINERAL_POWER",
    "REPAIR_POWER",
    "DISMANTLE_POWER",
    "BUILD_POWER",
    "ATTACK_POWER",
    "UPGRADE_CONTROLLER_POWER",
    "RANGED_ATTACK_POWER",
    "HEAL_POWER",
    "RANGED_HEAL_POWER",
    "REPAIR_COST",
    "DISMANTLE_COST",
    "RAMPART_DECAY_AMOUNT",
    "RAMPART_DECAY_TIME",
    "RAMPART_HITS",
    "RAMPART_HITS_MAX",
    "ENERGY_REGEN_TIME",
    "ENERGY_DECAY",
    "SPAWN_HITS",
    "SPAWN_ENERGY_START",
    "SPAWN_ENERGY_CAPACITY",
    "CREEP_SPAWN_TIME",
    "SPAWN_RENEW_RATIO",
    "SOURCE_ENERGY_CAPACITY",
    "SOURCE_ENERGY_NEUTRAL_CAPACITY",
    "SOURCE_ENERGY_KEEPER_CAPACITY",
    "CONSTRUCTION_COST_ROAD_SWAMP_RATIO",
    "ROAD_HITS",
    "ROAD_WEAROUT",
    "ROAD_DECAY_AMOUNT",
    "ROAD_DECAY_TIME",
    "RAMPART_DECAY_AMOUNT",
    "RAMPART_DECAY_TIME",
    "RAMPART_HITS",
    "RAMPART_HITS_MAX",
    "WALL_HITS",
    "WALL_HITS_MAX",
    # JavaScript things
    "typeof",
    "require",
    "module",
    "JSON",
    "this",
    "RegExp",
    "Array",
    "Error",
    "Infinity",
    "console",
    "undefined",
    "Map",
    "Set",
    "isFinite",
    "js_isNaN",
    "_",
    # Transcrypt-specific things
    "__pragma__",
    "__new__",
    "__except__",
    "__except0__",
    # Utility functions for autocomplete
    "new_map",
    "new_set",
]


class JSMap:
    def has(self, key):
        """
        :type key: Any
        :rtype: bool
        """

    def get(self, key):
        """
        :type key: Any
        :rtype: Any
        """

    def set(self, key, value):
        """
        :type key: Any
        :type value: Any
        :rtype: None
        """

    def delete(self, key):
        """
        :type key: Any
        """

    def entries(self):
        """
        :rtype: list[(Any, Any)]
        """

    def keys(self):
        """
        :rtype: list[Any]
        """

    def values(self):
        """
        :rtype: list[Any]
        """


class JSSet:
    def has(self, key):
        """
        :type key: Any
        :rtype: bool
        """

    def add(self, key):
        """
        :type key: Any
        :rtype: Any
        """

    def keys(self):
        """
        :rtype: list[Any]
        """

    def values(self):
        """
        :rtype: list[Any]
        """


__pragma__('noskip')


def new_map(iterable=undefined):
    """
    :rtype: JSMap
    """
    return __new__(Map(iterable))


def new_set(iterable=undefined):
    """
    :rtype: JSSet
    """
    return __new__(Set(iterable))
