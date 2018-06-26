from defs import *
import consts

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')



# Refills creeps store of resources
# Builder, Upgrader can use
def refill(me):
    #Targets containers first
    target = me.pos.findClosestByPath(FIND_STRUCTURES,
            {'filter' : lambda s: s.structureType == STRUCTURE_CONTAINER
                                  and s.store.energy >= me.carryCapacity})
    if target != None:
        code = me.withdraw(target, 'energy')
        if code == 0:
            pass
        elif code == ERR_NOT_IN_RANGE:
            me.moveTo(target)
        else:
            me.say('ERROR:', code)
        return True

    
    #Target dropped energy next
    target = me.pos.findClosestByPath(FIND_DROPPED_RESOURCES,
            {'filter': lambda r:
             r.resourceType == RESOURCE_ENERGY
             and r.amount >= me.carryCapacity})
    if target != None:
        code = me.pickup(target)
        if code == OK:
            pass
        elif code == ERR_NOT_IN_RANGE:
            me.moveTo(target)
        return True


    '''        
    #Otherwise, mine some
    target = me.pos.findClosestByPath(FIND_SOURCES_ACTIVE)
    if me.harvest(target) == ERR_NOT_IN_RANGE:
        me.moveTo(target)
    '''



def containerIsMineDrop(container):
    mineDrop = False
    for key, source in _.pairs(container.room.find(FIND_SOURCES)):
        if container.pos.isNearTo(source):
            mineDrop = True
    return mineDrop
    



def dm(message, indentLevel):
    if consts.DEBUG_MESSAGES:
        for i in range(indentLevel):
            message = '   ' + message
        print(message)



def getSpawnEnergy(me):
    total = 0
    for key, structure in _.pairs(me.room.find(FIND_STRUCTURES, {'filter':
            lambda s: s.structureType == STRUCTURE_EXTENSION
            or s.structureType ==  STRUCTURE_SPAWN})):
        total += structure.energy
    return total



def getSpawnEnergyCapacity(me):
    total = 0
    for key, structure in _.pairs(me.room.find(FIND_STRUCTURES, {'filter':
            lambda s: s.structureType == STRUCTURE_EXTENSION
            or s.structureType ==  STRUCTURE_SPAWN})):
        total += structure.energyCapacity
    return total



def getStoredEnergy(me):
    total = 0
    for key, container in _.pairs(me.room.find(FIND_STRUCTURES, {'filter':
            lambda s: s.structureType == STRUCTURE_CONTAINER})):
        total += container.store.energy
    for key, resource in _.pairs(me.room.find(FIND_DROPPED_RESOURCES,{'filter':
            lambda r: r.resourceType == RESOURCE_ENERGY})):
        total += resource.amount
    return total



def getAvgWallStrength(me):
    wallHits = []
    for key, wall in _.pairs(me.room.find(FIND_STRUCTURES, {'filter': lambda s:
            s.structureType == STRUCTURE_WALL})):
        wallHits.add(wall.hits)
    return sum(wallHits)/len(wallHits)



def constructionSitesExist(me):
    return not (me.pos.findClosestByRange(FIND_CONSTRUCTION_SITES) == None)
