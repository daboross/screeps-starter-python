from ...defs import *

class Creep:
    def __init__(self, name):
        self.name = name
        self.obj = Game.creeps[name]
        self.memory = self.obj.memory
        self.pos = self.obj.pos
        self.store = self.obj.store

    def run(self):
        pass

    def me(self):
        return self.ojb

    def get_next_name(self):
        prefix = type(self).__name__ + '_'
        i = 1
        while i in Game.creeps:
            i += 1
        return str(prefix + str(i))
