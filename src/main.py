# defs is a package which claims to export all constants and some JavaScript objects, but in reality does
#  nothing. This is useful mainly when using an editor like PyCharm, so that it 'knows' that things like Object, Creep,
#  Game, etc. do exist.
from defs import *

# These are currently required for Transcrypt in order to use the following names in JavaScript.
# Without the 'noalias' pragma, each of the following would be translated into something like 'py_Infinity' or
#  'py_keys' in the output file.
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')




###############################################################################################################################
#    MY CODE
###############################################################################################################################

from shared_methods import dm
import consts
import towerControl
import harvester
import static_harvester
import hauler
import upgrader
import builder
import manual1
import manual2
import manual3

#Run each tick.
def main():
    harvesters = 0
    static_harvesters = 0
    haulers = 0
    upgraders = 0
    builders = 0
    

    #MEMORY CONTROL
    #  Cleanup
    for name, creep in _.pairs(Memory.creeps):
        if not (name in Game.creeps):
            del Memory.creeps[name]


    #CREEP CONTROL
    for creepName in Object.keys(Game.creeps):
        creep = Game.creeps[creepName]

        if creep.memory.role == 'harvester':
            harvester.run(creep)
            harvesters += 1
        if creep.memory.role == 'static_harvester':
            static_harvester.run(creep)
            static_harvesters += 1
        if creep.memory.role == 'hauler':
            hauler.run(creep)
            haulers += 1
        if creep.memory.role == 'upgrader':
            upgrader.run(creep)
            upgraders += 1
        if creep.memory.role == 'builder':
            builder.run(creep)
            builders += 1
        if creep.memory.role == 'manual':
            manual1.run(creep)


    #TOWER CONTROL
    for key, room in _.pairs(Game.rooms):
        for key2, tower in _.pairs(room.find(FIND_STRUCTURES, {'filter':
                lambda s: s.structureType == STRUCTURE_TOWER})):
            towerControl.run(tower)


    #SPAWN CONTROL
    for spawnName in Object.keys(Game.spawns):
        spawn = Game.spawns[spawnName]

        #If already spawning, skip.
        if spawn.spawning != None:
            continue

        #If there are not enough of a certain class, spawn it
        if harvesters < consts.TARGET_HARVESTERS:
            spawn.spawnCreep(harvester.BODY_1, nameCreep('harvester'),
                              {'memory': {'role' : 'harvester'}})
        elif static_harvesters < consts.TARGET_STATIC_HARVESTERS:
            spawn.spawnCreep(static_harvester.BODY_0,
                             nameCreep('static_harvester'),
                             {'memory': {'role' : 'static_harvester'}})
        elif haulers < consts.TARGET_HAULERS:
            spawn.spawnCreep(hauler.BODY_2,
                             nameCreep('hauler'),
                             {'memory': {'role' : 'hauler'}})
        elif upgraders < consts.TARGET_UPGRADERS:
            spawn.spawnCreep(upgrader.BODY_2, nameCreep('upgrader'),
                             {'memory' : {'role' : 'upgrader'}})
        elif builders < consts.TARGET_BUILDERS:
            spawn.spawnCreep(builder.BODY_2, nameCreep('builder'),
                             {'memory': {'role' : 'builder'}})
        
    dm(' ',0)
           
def nameCreep(role):
    if role == 'harvester':
        target = consts.TARGET_HARVESTERS
    elif role == 'static_harvester':
        target = consts.TARGET_STATIC_HARVESTERS
    elif role == 'hauler':
        target = consts.TARGET_HAULERS
    elif role == 'upgrader':
        target = consts.TARGET_UPGRADERS
    elif role == 'builder':
        target = consts.TARGET_BUILDERS

    pre = role[0].upper() + role[1:] + ' '

    i = 0
    while True:
        i += 1
        
        name = str(pre + str(i))
        if name in Game.creeps:
            continue
        else:
            return name


module.exports.loop = main









