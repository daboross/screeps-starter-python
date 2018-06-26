from defs import *
from shared_methods import dm, getAvgWallStrength, getStoredEnergy
from shared_methods import getSpawnEnergyCapacity

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def run(me):
    dm(me.id + ' RUN')
    task = decideTask(me)
    if task == 'attack': attack(me)
    elif task == 'build': build(me)
    elif task == 'repair': repair(me)
    else: print('UNRECOGNISED TASK FOR TOWER')
    dm(me.id + ' END')
        


# Switch task if necessary:
def decideTask(me):
    if (me.pos.findClosestByRange(FIND_HOSTILE_CREEPS) != None
            or me.pos.findClosestByRange(FIND_HOSTILE_STRUCTURES) != None
            or me.pos.findClosestByRange(FIND_HOSTILE_CONSTRUCTION_SITES) != None):
        return 'attack'
    else:
        return 'repair'
       


def attack(me):
    target = me.pos.findClosestByRange(FIND_HOSTILE_CREEPS)
    if target != None:
        me.attack(target)



def repair(me):
    #Get target
    target = me.pos.findClosestByRange(FIND_STRUCTURES, {'filter': lambda s :
        s.hits < s.hitsMax and s.structureType != STRUCTURE_WALL})

    if target == None and getStoredEnergy(me) > getSpawnEnergyCapacity(me):
        target = me.pos.findClosestByRange(FIND_STRUCTURES, {'filter': lambda s :
            s.hits < s.hitsMax and s.hits < getAvgWallStrength(me)})

    if target!= None:
        me.repair(target)
