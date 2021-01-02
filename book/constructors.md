# Object Creation

While Transcrypt supports standard Python syntax for class instance creation and use, the JavaScript syntax for creating new objects must be used when interacting with a small number of Screeps prototypes.  In Python, new objects are created by calling the class; in JavaScript, to create an instance of an object, the `new` keyword must be provided along with a call to the contruct that creates the object.  

Transcrypt provides a method, `__new__()`, that supports creating interacting with constructors in third party libraries.  When working with code examples provided by the API, any instance of `new Constructor()` should be replaced with `__new__(Constructor())`.

#### Examples
 
_Creating a new [RoomPosition](http://docs.screeps.com/api/#RoomPosition) object:_

```py
room_pos = __new__(RoomPosition(25, 25, 'E34S25'))
```

_Creating a new [RoomVisual](http://docs.screeps.com/api/#RoomVisual):_
```py
# Displays the current tick in the upper-left corner of all rooms
 __new__(RoomVisual().text(Game.time, 0, 0, {'align': 'left', 'font': 0.6}))
 ```
 
_Creating a new [CostMatrix](http://docs.screeps.com/api/#PathFinder-CostMatrix):_
```py
costs = __new__(PathFinder.CostMatrix)
```