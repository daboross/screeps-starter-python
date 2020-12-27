# Optional Arguments

Most methods provided through the API support a number of different optional arguments that that augment the behavior and/or return results of the process being called. Most optional arguments are provided through predefined variables that are grouped together in a single object.

JavaScript does not natively support named keyword arguments like Python; so all named optional arguments must be provided using the single object format.

## Predefined Variable Syntax

All predefined optional argument variable names must be provided as strings; while this isn't necessary when writing screeps code in JavaScript, failing to provide arguments as strings will either cause `build.py` to fail, or, Screeps itself won't recognize the variable name. This rule holds true for every API call except for arguments that allow for a custom `CostMatrix`; you can read more about this in the `PathFinder - CostMatrix` section.

### Examples

_Modifying `.moveTo()` behavior:_

```python
creep.moveTo(creep.room.controller, {'maxRooms': 1, 'ignoreCreeps': True})
```

_Spawning a creep with predefined memory:_

```python
name = "{}{}".format('harvester', Game.time)
spawn.spawnCreep([WORK, CARRY, MOVE], name, {'memory': {'role': 'harvester'}})
```

