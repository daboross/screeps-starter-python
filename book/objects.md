# Objects

Entities in the game world exist as object prototypes; if you've never used JavaScript before, you can think of these like instances of a class in Python.  Prototypes have both attributes and methods and are accessed in JavaScript like they are in Python.

#### Syntax:

_Referencing a specific spawn through a variable:_

```py
spawn = Game.spawns.Spawn1
```

_Moving a Creep:_

```py
creep = Game.creeps['upgrader123']
creep.moveTo(creep.room.controller)
```


