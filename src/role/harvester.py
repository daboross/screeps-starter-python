from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def run(creep: Creep):
    if creep.store.getFreeCapacity() > 0:
        sources = creep.room.find(FIND_SOURCES)
        if creep.harvest(sources[0]) == ERR_NOT_IN_RANGE:
            creep.moveTo(
                sources[0], {'visualizePathStyle': {'stroke': '#ffaa00'}})
    else:
        targets = creep.room.find(FIND_STRUCTURES, {
            'filter': lambda structure: (
                (
                    structure.structureType == STRUCTURE_EXTENSION or
                    structure.structureType == STRUCTURE_SPAWN or
                    structure.structureType == STRUCTURE_TOWER
                ) and
                structure.store.getFreeCapacity(RESOURCE_ENERGY) > 0
            )
        })
        if len(targets) > 0:
            if creep.transfer(targets[0], RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                creep.moveTo(
                    targets[0], {'visualizePathStyle': {'stroke': '#ffffff'}})
