# Constants

Screeps provides a number of [constants](http://docs.screeps.com/api/#Constants) that hold references to everything from error codes to in-game resources. The constants themselves either store some kind of value \(like a string or integer\) or are a reference to data structures like arrays and objects. Some constants are provided for conveince while others are required for some API calls.

Unlike optional named arguments, constants should be provided as is; constants are always uppercase with individual words seperated by underscores.

## Examples

_Defining a creep's part list:_

```python
harvester_parts = [WORK, MOVE, CARRY]
```

_Referencing a resource and checking for an error code:_

```python
if creep.withdraw(creep.room.storage, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
    creep.moveTo(creep.room.storage)
```

