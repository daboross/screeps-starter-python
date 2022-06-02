# defs is a package which claims to export all constants and some JavaScript objects, but in reality does
#  nothing. This is useful mainly when using an editor like PyCharm, so that it 'knows' that things like Object, Creep,
#  Game, etc. do exist.

from defs import *

# These are currently required for Transcrypt in order to use the following names in JavaScript.
# Without the 'noalias' pragma, each of the following would be translated into something like 'py_Infinity' or
#  'py_keys' in the output file.
from subcontrollers.creep.starter import Starter

from subcontrollers.structure.spawner import Spawner

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def main():
    memory_cleanup()
    [spawner.run() for spawner in get_spawners()]
    [creep.run() for creep in get_creeps()]


def memory_cleanup():
    for creep in Object.keys(Memory.creeps):
        if not (creep in Game.creeps):
            del Memory.creeps[creep]


def get_spawners():
    spawns = []
    for spawn_name in Object.keys(Game.spawns):
        spawns.append(Spawner(spawn_name))
    return spawns


def get_creeps():
    creeps = []
    for creep in Object.keys(Game.creeps):
        prefix = creep.split('_')[0]
        if prefix == 'Starter':
            creeps.append(Starter(creep))
    return creeps


module.exports.loop = main
