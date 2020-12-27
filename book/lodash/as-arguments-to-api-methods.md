# As Arguments to API Methods

In addition to accepting standard optional arguments that modify some specific aspect of an API call, methods that return an array of objects \(most notably `find*()` methods\) accept a Lodash filter as an optional argument. While the example syntax provided by the game will not work in your Python code, only minor changes are needed to produce a similar result.

## Examples

_Finding all extensions in a room:_

```python
extensions = creep.room.find(FIND_STRUCTURES, {
    "filter": lambda s: 
        s.structureType == STRUCTURE_ROAD
})
```

_Finding the closest dropped resource that meets a multiple criteria:_

```python
dropped_energy = creep.pos.findClosestByRange(FIND_DROPPED_RESOURCES, {
    "filter": lambda r: 
        r.resourceType == RESOURCE_ENERGY and r.amount >= 100
    })
```

