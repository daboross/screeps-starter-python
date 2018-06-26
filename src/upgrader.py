from defs import *
from shared_methods import refill
from shared_methods import dm

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

BODY_0 = [MOVE, WORK, CARRY]
BODY_1 = [MOVE, MOVE, MOVE, WORK, WORK, CARRY, CARRY, CARRY, CARRY]
BODY_2 = [MOVE,MOVE,MOVE,MOVE,MOVE,MOVE,WORK,WORK,CARRY,CARRY,CARRY,
          CARRY,CARRY,CARRY]

def run(me):
    dm(me.name + ' RUN', 0)
    decideTask(me)
    if me.memory.upgrading: upgrade(me)
    else: refill(me)
    dm(me.name + ' END', 0)
        


# Switch task if necessary:
def decideTask(me):
    if me.carry.energy == 0:
        if me.memory.upgrading: me.say('Refilling')
        me.memory.upgrading = False
    elif me.carry.energy == me.carryCapacity:
        if not me.memory.upgrading: me.say('Upgrading')
        me.memory.upgrading = True



def upgrade(me):
    target = me.room.controller
    if me.upgradeController(target, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
        me.moveTo(target)
