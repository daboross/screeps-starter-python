from ...subcontrollers.creep.starter import Starter
from ...defs import *


class Spawner:
    def __init__(self, name):
        self.name = name
        self.obj = Game.spawns[name]

    def run(self):
        if self.obj.spawning is None:
            self._spawn_creep([MOVE, MOVE, WORK, CARRY, CARRY], Starter)

    def _spawn_creep(self, body, role):
        result = self.obj.spawnCreep(body, self._next_name(role), {'memory': role.DEFAULT_MEMORY})

    def _next_name(self, role):
        prefix = role.__name__ + '_'
        i = 1
        while prefix + str(i) in Game.creeps:
            i += 1
        return prefix + str(i)
