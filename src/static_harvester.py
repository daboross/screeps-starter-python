from defs import *
from shared_methods import containerIsMineDrop
from shared_methods import dm

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

BODY_0 = [WORK, WORK, WORK, WORK, WORK, MOVE]

def run(me):
    dm(me.name + ' RUN')
    #If no target, get one
    if me.memory.target == None:
         initialise(me)

    #If not in position, move
    
    if (me.pos.x != Game.getObjectById(me.memory.target).pos.x
        or me.pos.y != Game.getObjectById(me.memory.target).pos.y):
        me.moveTo(Game.getObjectById(me.memory.target))

    #If in position, mine
    else:
        target = me.pos.findClosestByPath(FIND_SOURCES)
        code = me.harvest(target)
        if code == OK or code == -6:
            pass
        else:
            me.say('ERROR', code)
    dm(me.name + ' END')


def initialise(me):
    dm('Initialising', 1)
    #For each container
    containers = me.room.find(FIND_STRUCTURES,
                              {'filter': lambda s: s.structureType
                               == STRUCTURE_CONTAINER})
    
    for key, container in _.pairs(containers):
        targeted = False

        dm('Container found: ' + container.id, 2)
        dm(container.id + ' is mine drop: ' +
           str(containerIsMineDrop(container)), 3)
        
        if containerIsMineDrop(container):
            #Determine if it is targeted yet 
            for key2, creep in _.pairs(Game.creeps):
                if creep.memory.role == 'static_harvester':

                    dm('Static harvester found: ' + creep.name, 3)
                    dm(creep.name + ' target: ' + creep.memory.target, 4) 
                    dm('Mine drop is creeps target: ' + str(creep.memory.target == container.id), 4)

                    if creep.memory.target == container.id:
                        targeted = True
                        break

            #If not target, target it.
            dm('Mine drop already targeted: ' + str(targeted), 3)
            if targeted == False:
                dm('TARGET SET: ' + container.id, 3)
                me.memory.target = container.id
