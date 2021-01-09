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
    if creep.memory.upgrading and creep.store[RESOURCE_ENERGY] == 0:
        creep.memory.upgrading = False
        creep.say('🔄 harvest')
    if not creep.memory.upgrading and creep.store.getFreeCapacity() == 0:
        creep.memory.upgrading = True
        creep.say('⚡ upgrade')

    if creep.memory.upgrading:
        if creep.upgradeController(creep.room.controller) == ERR_NOT_IN_RANGE:
            creep.moveTo(creep.room.controller,
                         {'visualizePathStyle': {'stroke': '#ffffff'}})
    else:
        sources = creep.room.find(FIND_SOURCES)
        if creep.harvest(sources[0]) == ERR_NOT_IN_RANGE:
            creep.moveTo(sources[0],
                         {'visualizePathStyle': {'stroke': '#ffaa00'}})
