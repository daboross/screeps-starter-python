from defs import *
from shared_methods import refill, dm, getStoredEnergy, getSpawnEnergyCapacity
from shared_methods import getAvgWallStrength, constructionSitesExist

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

BODY_0 = [MOVE,WORK,CARRY]
BODY_1 = [MOVE,MOVE,MOVE,WORK,WORK,CARRY,CARRY,CARRY,CARRY]
BODY_2 = [MOVE,MOVE,MOVE,MOVE,WORK,WORK,WORK,WORK,CARRY,CARRY,CARRY,CARRY]

def run(me):
    dm(me.name + ' RUN', 0)
    decideTask(me)
    if  me.memory.task == 'build': build(me)
    elif me.memory.task == 'repair': repair(me)
    elif me.memory.task == 'refill': refill(me)
    else: me.say('ERROR', me.memory.task)
    dm(me.name + ' END', 0)



# Switch task if necessary:
def decideTask(me):
    if me.carry.energy == 0:
        if me.memory.task == 'build': me.say('Refilling')
        me.memory.task = 'refill'
    else:
        if constructionSitesExist(me):
            if me.memory.task != 'build': me.say('Building')
            me.memory.task = 'build'
        else:
            if me.memory.task != 'repair': me.say('Repairing')
            me.memory.task = 'repair'    



# Finds and builds constructions
def build(me):
    target = me.pos.findClosestByRange(FIND_CONSTRUCTION_SITES)
    if target!= None:
        if me.build(target) == ERR_NOT_IN_RANGE:
            me.moveTo(target)



# Repairs structures
def repair(me):
    #Get target
    target = me.pos.findClosestByRange(FIND_STRUCTURES, {'filter': lambda s :
        s.hits < s.hitsMax and s.structureType == STRUCTURE_WALL
        and s.hits < getAvgWallStrength(me) + 50})

    if target == None:
        target = me.pos.findClosestByRange(FIND_STRUCTURES, {'filter': lambda s :
        s.hits < s.hitsMax})

    if target!= None:
        if me.repair(target) == ERR_NOT_IN_RANGE:
            me.moveTo(target)
