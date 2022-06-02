from ...defs import *
from ...subcontrollers.creep.creep import Creep


class Starter(Creep):
    DEFAULT_MEMORY = {'collecting': True}

    def __init__(self, name):
        super().__init__(name)

    def run(self):
        if self.memory.collecting:
            self.collect()
        else:
            self.deposit()

    def collect(self):
        target = self.pos.findClosestByPath(FIND_SOURCES_ACTIVE)
        code = self.obj.harvest(target)
        if code == OK:
            if self.obj.store.getFreeCapacity() == 0:
                self.obj.say('Dropping')
                self.memory.collecting = False
        if code == ERR_NOT_IN_RANGE:
            self.obj.moveTo(target)

    def deposit(self):
        target = self.get_target()
        code = self.obj.transfer(target, RESOURCE_ENERGY)
        if code == OK:
            self.obj.say('Collecting')
            self.memory.collecting = True
        if code == ERR_NOT_IN_RANGE:
            self.obj.moveTo(target)

    def get_target(self):
        return Game.spawns['Spawn1']
