from defs import *

"""
This class represents the basic behaviors and actions common to all WorkerCreeps
"""
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


class CreepBase:
    def __init__(self):
        self.role = None
        self.memory_blueprint = None  # dict for initial memory when creating new creeps of this type
        self.body_blueprint = None  # list of body part constants that construct this creep
        self.creep = None  # The inner creep object for accessing creep commands

    def spawn(self, target_spawner_name, dry_run=False):
        if self.canSpawn(target_spawner_name):
            creep_name = self.getNewName()
            console.log('Spawning:{0}'.format(creep_name))
            opts = {"memory": self.memory_blueprint, "dryRun": dry_run}
            spawn_successful = Game.spawns[target_spawner_name].spawnCreep(self.body_blueprint, creep_name, opts)
            return spawn_successful

    def canSpawn(self, target_spawner_name):
        opts = {"memory": self.memory_blueprint, "dryRun": True}
        can_spawn = Game.spawns[target_spawner_name].spawnCreep(self.body_blueprint, 'spawn_test', opts)
        return can_spawn

    def getNewName(self):
        return '_'.join(self.role, Game.time)

    def getCarryAmount(self):
        return _.sum(self.creep.carry)

    def getLiveCreeps(self):
        these_creeps = _.filter(Game.creeps, lambda creep: creep.memory.role == this.role)
        return these_creeps