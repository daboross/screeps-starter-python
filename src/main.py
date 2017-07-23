import harvester
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


def main():
    """
    Main game logic loop.
    """

    # Run each creep
    for name in Object.keys(Game.creeps):
        creep = Game.creeps[name]
        harvester.run_harvester(creep)

    # Run each spawn
    for name in Object.keys(Game.spawns):
        spawn = Game.spawns[name]
        if not spawn.spawning:
            # Get the number of our creeps in the room.
            num_creeps = _.sum(Game.creeps, lambda c: c.pos.roomName == spawn.pos.roomName)
            # If there are no creeps, spawn a creep once energy is at 250 or more
            if num_creeps < 0 and spawn.room.energyAvailable >= 250:
                spawn.createCreep([WORK, CARRY, MOVE, MOVE])
            # If there are less than 15 creeps but at least one, wait until all spawns and extensions are full before
            # spawning.
            elif num_creeps < 15 and spawn.room.energyAvailable >= spawn.room.energyCapacityAvailable:
                # If we have more energy, spawn a bigger creep.
                if spawn.room.energyCapacityAvailable >= 350:
                    spawn.createCreep([WORK, CARRY, CARRY, MOVE, MOVE, MOVE])
                else:
                    spawn.createCreep([WORK, CARRY, MOVE, MOVE])


module.exports.loop = main
