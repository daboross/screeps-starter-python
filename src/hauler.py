from defs import *
from shared_methods import containerIsMineDrop, dm, getSpawnEnergy
from shared_methods import getSpawnEnergyCapacity, getStoredEnergy


__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

BODY_0 = [MOVE, CARRY]
BODY_1 = [MOVE, MOVE, MOVE, MOVE, MOVE, CARRY, CARRY, CARRY, CARRY, CARRY]
BODY_2 = [MOVE,MOVE,MOVE,MOVE,MOVE,MOVE,MOVE,MOVE,CARRY,CARRY,CARRY,CARRY,
          CARRY,CARRY,CARRY,CARRY]

def run(me):
    dm(me.name + ' RUN', 0)
    decideTask(me)
    if me.memory.depositing: deposit(me)
    else: refill(me)
    dm(me.name + ' END', 0)



def decideTask(me):
    if me.carry.energy == 0:
        if me.memory.depositing: me.say('Refilling')
        me.memory.depositing = False
    elif me.carry.energy == me.carryCapacity:
        if not me.memory.depositing: me.say('Dropping')
        me.memory.depositing = True



def deposit(me):
    target = getDropTarget(me)
    if target == False:
        queueByExtension(me)
    else:
        code = me.transfer(target, RESOURCE_ENERGY)
        if code == OK:
            me.memory.target = False
        elif code == ERR_NOT_IN_RANGE:
            me.moveTo(target)
        else:
            me.say('ERR', code)



def refill(me):
    out = getCollectTarget(me)

    if out == None:
        me.say('NO TARGET. CHECK THIS IS RIGHT')
        return

    target = out[0]
    targetType = out[1]

    if targetType == 'floor':
        code = me.pickup(target)
    elif targetType == 'container':
        code = me.withdraw(target, 'energy')
    else:
        me.say('ERROR - BAD TARGET')

    if code == 0:
        pass
    elif code == ERR_NOT_IN_RANGE:
        me.moveTo(target)
    else:
        me.say(code)
    return True



def getDropTarget(me):
    #SPAWNS
    if Game.spawns['Spawn1'].energy < Game.spawns['Spawn1'].energyCapacity:
        return Game.spawns['Spawn1']

    #EXTENSIONS
    target = me.pos.findClosestByPath(FIND_STRUCTURES, {'filter': lambda s:
        s.structureType == STRUCTURE_EXTENSION and s.energy < s.energyCapacity})
    if target != None:
        return target

    #TOWERS
    target = me.pos.findClosestByPath(FIND_STRUCTURES, {'filter': lambda s:
        s.structureType == STRUCTURE_TOWER
        and (s.energyCapacity - s.energy) > 200})
    if target != None:
        return target

    #CONTAINERS
    target = me.pos.findClosestByPath(FIND_STRUCTURES, {'filter': lambda s:
        s.structureType == STRUCTURE_CONTAINER
        and s.store.energy < s.storeCapacity
        and containerIsMineDrop(s) == False})
    if target != None:
        return target

    return False


    
def getCollectTarget(me, fillCarry = True):
    dm('Getting collection target',1)
    
    #IF SPAWN OR TURRET NEEDS FILLING: SETS TARGET TO CLOSEST CONTAINER
    takeFromStorage = False
    if getSpawnEnergy(me) < getSpawnEnergyCapacity(me):
        takeFromStorage = True
    elif len(me.room.find(FIND_STRUCTURES, {'filter': lambda s:
                s.structureType == STRUCTURE_TOWER
                and (s.energyCapacity - s.energy) > me.carryCapacity})) > 0:
        takeFromStorage = True
            
    if takeFromStorage:
        target = me.pos.findClosestByPath(FIND_STRUCTURES,
                {'filter': lambda s: s.structureType
                 == STRUCTURE_CONTAINER
                 and s.store.energy >= me.carryCapacity})

    if target != None:
        return (target, 'container')
    
    #SETS TARGET TO CLOSEST DROPPED ENERGY THAT FILLS CARRY.
    if fillCarry:
        target = me.pos.findClosestByPath(FIND_DROPPED_RESOURCES,
                {'filter': lambda r:
                 r.resourceType == RESOURCE_ENERGY
                 and r.amount >= me.carryCapacity})
    else:
        target = me.pos.findClosestByPath(FIND_DROPPED_RESOURCES,
                {'filter': lambda r:
                 r.resourceType == RESOURCE_ENERGY})
        
    if target != None:
        return (target, 'floor')


    #SETS TARGET TO CLOSEST MINE DROP.
    if fillCarry:
        target = me.pos.findClosestByPath(FIND_STRUCTURES,
                {'filter': lambda s: s.structureType
                 == STRUCTURE_CONTAINER
                 and containerIsMineDrop(s)
                 and s.store.energy >= me.carryCapacity})
    else:
        target = me.pos.findClosestByPath(FIND_STRUCTURES,
                {'filter': lambda s: s.structureType
                 == STRUCTURE_CONTAINER
                 and containerIsMineDrop(s)
                 and s.store.energy > 0})

    if target != None:
        return (target, 'container')

    if fillCarry:
        return getCollectTarget(me, False)
    else: return False

   
def queueByExtension(me):
    for key, point in _.pairs(Game.structures):
        pointTargeted = False

        #If it is an extension
        if (point.structureType == STRUCTURE_EXTENSION):
           
            #If no creep targets it
            for creepName in Object.keys(Game.creeps):
                creep = Game.creeps[creepName]
                
                if creep.memory.target == point:
                    pointTargeted = True

            #Target it
            if pointTargeted == False:
                me.memory.target = point
                return point

    #If there is no suitible extension to queue at, queue at spawn.
    me.memory.target = Game.spawns['Spawn1']
    return Game.spawns['Spawn1']
