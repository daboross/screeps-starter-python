# Overview
In addition to supporting all API calls, The in-game console also allows you to call your own functions and methods.  While your function/method can be defined in any file, it must be imported into `main.py` and added as an entry to a special object, `js_global`, which holds references to all API prototypes, objects, constants, and so on.  

You can call anything defined in `js_global` like you would a normal function.  If you want to instantiate and class and call a method from the console, make all the necessary calls to the class from a function, and then store a reference to that function in `js_global` like you would a normal function call.  

#### Example

_controller_properties.py_

```py
from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def get_controller_level(room_name):
    """Returns the controller level for Game.rooms[room_name]"""
    
    room = Game.rooms[room_name]
    
    if room and room.controller:
        return room.controller.level
    else:
        return "Error: no access too {}".format(room_name)                
```

_main.py_

```py
import controller_properties
from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

# Create a new entry for each new command
js_glboal.get_controller_level = controller_properties.get_controller_level

def main():
    """You normal screeps code here"""
    pass
    
module.exports.loop = main
```

#### js_global

`js_global` is a reference to a JavaScript `global` object, which is a globally scoped object that is always available to be referenced. Because `global` is already a keyword in Python, this alternate version is used.  You can check the contents of `js_global` in-game at any time by entering `global` in the in-game console, but any time you want to reference it in your code, `js_global` must be used instead.

